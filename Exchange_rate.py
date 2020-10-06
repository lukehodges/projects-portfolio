import requests
exchange = requests.get('https://open.exchangerate-api.com/v6/latest').json()
for i in exchange['rates'].items():
	print('1 usd: {} {}'.format(i[1],i[0]))
