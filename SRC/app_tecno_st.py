import sqlite3
import json
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
conn=sqlite3.connect("MobileProduct.db")
df=pd.read_sql("select * from MobileData",conn)
cols=st.columns(4)
for i,row in df.iterrows():
    with cols[i%4]:
        st.image(row["image"])
        st.write(row["title"])
        st.write(row["price"])
        features = json.loads(row["features"])
        for key, value in features.items():
            st.write(f"**{key}:** {value}")
        st.link_button("View",row["link"])