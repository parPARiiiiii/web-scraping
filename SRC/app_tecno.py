import requests
import sqlite3
import json

from bs4 import BeautifulSoup

url = 'https://www.technolife.com/category/mobile/mobile-phone'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup)

DB_NAME = 'MobileProduct.db'
conn = sqlite3.connect(DB_NAME)
print('DB CREATED')


query = '''
CREATE TABLE IF NOT EXISTS MobileData
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price TEXT,
    image TEXT,
    link TEXT,
    features TEXT
)
'''
cursor = conn.cursor()
cursor.execute(query)
conn.commit()
# conn.close()

print('TABLE CREATED')

cards = soup.select('section.relative.w-full.rounded-\\[10px\\]')
# print('cards: ', len(cards))

for card in cards:
    title = card.find('h2').text.strip()
    if title == None:
        continue

    # print(title)

    price = card.select_one('p.text-\\[22px\\].font-semiBold.leading-5').text.strip()
    if price == None:
        continue

    # print(price)

    image = card.select_one('a[href^="/product-"] img').get('src')
    img_url = 'https://www.technolife.com' + image

    # print(img_url)
    link = 'https://www.technolife.com' + card.select_one('a[href^="/product-"]').get('href')


    product_response = requests.get(link)
    product_soup = BeautifulSoup(product_response.text, 'html.parser')
    features = product_soup.find('h2', string=lambda x: x and 'ویژگی‌های اصلی' in x)

    container = features.find_next_sibling('div')

    rows = container.find_all('div', recursive=False)

    features = {}

    for row in rows:
        values = row.find_all('p', recursive=False)

        if len(values) >= 2:
            key = values[0].get_text(strip=True)
            value = values[1].get_text(strip=True)
            features[key] = value
    features_json = json.dumps(features, ensure_ascii=False)
    query = '''
        INSERT INTO MobileData(title, price, image, link, features) 
        VALUES(?, ?, ? , ?, ?)
        '''
    cursor.execute(query, (title, price, img_url, link, features_json))
    conn.commit()

conn.close()
print('WEB DATA Scraped')
