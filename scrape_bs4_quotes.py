from bs4 import BeautifulSoup
import requests

response=requests.request("GET","https://quotes.toscrape.com/")
html=response.text
soup=BeautifulSoup(html,'html.parser')
for tags in soup.findAll('span',{'class':'text'}):
    print(tags.string)

