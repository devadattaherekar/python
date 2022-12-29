import requests

uri=f"https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=in&lang=en&page=1&records=10"
response=requests.get(uri)
html=response.text
print(type(html))
html=response.json()
print(type(html))
for records in html['results']:
    print(records['title'])

