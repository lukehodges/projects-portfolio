import fortnite_api,pprint
pp = pprint.PrettyPrinter(indent=4)


api = fortnite_api.FortniteAPI()# create api for using fortnite_api

cosmetics = list(map(lambda x: api.cosmetics.fetch_all(),range(1)))# collect cosmetics

shop = api.shop.fetch()

daily = shop.daily.entries
for item in daily:
	print('bundle price: ({} VBucks)'.format(item.final_price))
	for part in item.items:
		print('	name: {}\n	type: {}\n'.format(part.name, str(part.type).split('.')[1]))
