import json

with open('data/test-009000.json') as data_file:
	data = json.load(data_file)
	with open('data/sorted-test.json', 'w') as out_file:
		json.dump(data, out_file, sort_keys=True)