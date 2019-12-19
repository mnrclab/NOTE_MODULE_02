import requests

host = 'https://developers.zomato.com/api/v2.1/'
kategori = '/categories'
apikey = 'a0db0542879222e54be4e96eeb888056'
headInfo = {
    'user-key': apikey
}

url = host + kategori
data = requests.get(url, headers=headInfo)

# print(data.json()['categories'])

x = []
for i in data.json()['categories']:
    x.append(i['categories']['name'])
print(x)

# TUGAS
'''
1. LOKASI TEMPAT MAKAN, MAU MAKAN APA?
2. digidb.io/digimon-list
3. w3school.com => html, minimal sampai classes

'''