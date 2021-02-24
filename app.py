import requests
import streamlit as st
from bs4 import BeautifulSoup

r = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(r.text,'lxml')

st.markdown('''
# News App using Steamlit and Python
Shown are the latest news.

**Credits**
- App built by [Baburaj R](https://wa.me/919567284082)
- Built in `Python` using `streamlit`, `requests` and `BeautifulSoup`
''')
st.write('---')

text = [x.text for x in soup.find_all('tr', class_='athing')]
links = [x['href'] for x in soup.find_all('a', class_='storylink', href=True)]
for i in range(30):
    st.markdown(text[i])
    st.write(links[i])
    st.write('\n')
    i = i+1