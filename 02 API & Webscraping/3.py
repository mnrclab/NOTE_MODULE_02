import requests

url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t=Liverpool'
data = requests.get(url)
print(data)

# print(data.json()['address'])
# print(data.json()['name'])
# print(type(data.json()))
# print(data.json()['address']['street'])


# for i in data.json():
#     print(i['name'], 'di Jl.', i['address']['street'])



# import requests
# klub = input('Ketik klub: ')
# url = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
# data = requests.get(url)
# players = data.json()['player']

# for player in players:
#     print(f"{player['strPlayer']} ({player['strPosition']})")


#API Key for Weather: 459d9e04c30f301451da1b16999bfc5b



# import requests
# url = 'http://quotes.rest/qod'
# data = requests.get(url)
# data = data.json()
# print(data)
# print(data['contents']['quotes'][])


# import requests

# x = '&appid=459d9e04c30f301451da1b16999bfc5b'
# y = input('Ketik kota: ')
# url = f'http://api.openweathermap.org/data/2.5/weather?q={y}{x}'
# data = requests.get(url)
# data = data.json()
# sunrise = data['sys']['sunrise']
# # sunset = data['sys']['sunset']

# from datetime import datetime
# waktu = datetime.utcfromtimestamp(int(sunrise))
# print(int(waktu.strftime('%d'))+1)
# print(int(waktu.strftime('%H'))+7-24)

