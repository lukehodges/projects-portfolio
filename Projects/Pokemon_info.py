import requests,pprint
url = requests.get('https://pokeapi.co/api/v2/pokemon/')
#pprint.pprint(url.json())
pokemon = input('enter the pokemon name> ')
try:
	pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
	pokemon.stats = pokemon.json()
	stats = pokemon.stats['stats']
	for i in stats:
		print('{} : {}'.format(i['stat']['name'],i['base_stat']))
except:
	pass
