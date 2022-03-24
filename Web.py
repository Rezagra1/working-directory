import re
from bs4 import BeautifulSoup
import requests

html_doc = requests.get('http://www.tsetmc.com/Loader.aspx?ParTree=151311&i=65883838195688438')

soup = BeautifulSoup(html_doc.text,'html.parser')


print(soup.h1)
