import requests
from bs4 import BeautifulSoup
import pandas as pd 

url="https://www.trendyol.com/sr?q=iphone"
response=requests.get(url)
html_icerigi=response.content
soup=BeautifulSoup(html_icerigi, "html.parser")
isim=soup.find_all("span", attrs={"class":"product-brand"})
print(isim)
