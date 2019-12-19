from bs4 import BeautifulSoup
import requests

web = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
data = BeautifulSoup(web.content, 'html.parser')
# print(data.prettify())

# for i in data.find_all('strong'):
#     print(i.text)

strong = data.find_all('strong')
daftar = []
for i in strong:
    daftar.append(i.text)

ultra = daftar[2:36]
monster = daftar[37:110]

print(ultra)
print(monster)