import requests 
from requests_html import HTMLSession
session = HTMLSession()

'''r = session.get("https://www.imdb.com/chart/top/") 
listerList = r.html.find('.lister-list',first=True)
print(listerList)

Title = listerList.find('.titleColumn')
print(Title)
Rating = listerList.find('.ratingColumn strong')
for i in range(0,len(Title)):
    
    print(Title[i].text)
    print(Rating[i].text)
    

img = listerList.find('.posterColumn a img')
for i in img:
    print(i.attrs['src'])'''

r = session.get("https://www.imdb.com/title/tt1187043/")
listerList = r.html.find('.title_bar',first=True)
print(listerList)

Title = listerList.find('.title_wrapper  ') 
print(Title)

for i in range(0,len(Title)):
    print(Title[i].text)