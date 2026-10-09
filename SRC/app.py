from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select('div.medium.widget.event.widget.last ul.menu li a')
print(titles)

for item in titles:
    print(item.get_text())
# print(soup)
# latest_news = soup.find('div', attrs={'class':'medium-widget blog-widget'})
# #print('len latest news', len(latest_news))
# # print(latest_news)

# titles = latest_news.find_all('a')
# # print(titles)

# times = latest_news.find_all('time')


# for item in titles:
#     print(item.get_text())
#     print(item.get('href'))
#     print('_'*30)

# for item in times:
#     print(item.get_text())
#     print('-'*30)




# upcoming_events = soup.find('div', attrs={'class':'medium-widget event-widget last'})

# titles_2 = upcoming_events.find_all('a')

# times_2 = upcoming_events.find_all('time')


# for item in titles_2:
#     print(item.get_text())
#     print(item.get('href'))
#     print('_'*30)

# for item in times_2:
#     print(item.get_text())
#     print('-'*30)