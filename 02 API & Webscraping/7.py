# WEB SCRAPPING FROM HTML FILE

from bs4 import BeautifulSoup
# data = BeautifulSoup(
#     open('coba.html', 'r'), 'html.parser'
#     )

# print(data)
# print(data.prettify())
# print(data.title)           #UNTUK MENAMPILKAN TAG 'TITLE'
# print(data.title.name)    #UNTUK MENAMPILKAN TAG DALAM FILE HTML
# print(data.title.text)    #UNTUK MENAMPILKAN TEXT SAJA PADA TAG 'TITLE'
# print(data.title.string)  #UNTUK MENAMPILKAN TEXT SAJA


# print(data.h1)           #UNTUK MENAMPILKAN TAG 'H1'
# print(data.h1.name)    #UNTUK MENAMPILKAN TAG DALAM FILE HTML
# print(data.h1.text)    #UNTUK MENAMPILKAN TEXT SAJA PADA TAG 'H1'
# print(data.h1.string)  #UNTUK MENAMPILKAN TEXT SAJA


# print(data.ul.text) #MENAMPILKAN ISI DATA DALAM LIST
# print(data.li.string)

# for x in data.find_all('li'):
#     print(x.text)

# ul = data.ul
# for i in ul.find_all('li'):
#     print(i.text)

# ===========================================
from bs4 import BeautifulSoup
data = BeautifulSoup(
    open('coba.html', 'r'), 'html.parser'
    )

# print(data.find(class_ = 'orang'))
# print(data.find('li', class_ = 'orang'))

# ul = data.ul 
# for i in ul.find_all('li', class_ = 'orang'):
#     print(i.text)

# ul = data.ul 
# for i in ul.find_all('li', class_ = 'orang'):
#     print(i['class'][0])

import requests

web = requests.get('http://127.0.0.1:5500/04.%20RawData_Module_02/coba.html')
# print(web.status_code)
# print(web.content)
data = BeautifulSoup(web.content, 'html.parser')
# print(data.prettify())

ul = data.ul 
for i in ul.find_all('li', id = 'person'):
    print(i.text)
