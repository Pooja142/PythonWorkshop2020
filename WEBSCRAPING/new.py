from requests_html import HTMLSession,HTMLResponse
import urllib.request 

session = HTMLSession()

response = session.get("http://books.toscrape.com/")
# print(response)

source = response.html 

# print(type(source))
# print(source)

block = source.find('ol.row', first=True)
# print(block)

name = []
cost = []
images = []

titles = block.find('li h3 a')
for title in titles:
    # print(title.attrs['title'])
    name.append(title.attrs['title'])


prices = block.find('li p.price_color')
for price in prices:
    # print(price.text[1:])
    cost.append(price.text[1:])



for i in range (len(name)):
    print(name[i])
    print(cost[i])
    






# urllib.request.urlretrieve(images[i], name[i])


