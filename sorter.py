import json

with open('data/ensemble.json') as data_file:
	data = json.load(data_file)
	with open('data/sorted-ensemble.json', 'w') as out_file:
		json.dump(data, out_file, sort_keys=True)