import json
from collections import Counter
categories = Counter()
reasoning = Counter()

with open('data/sorted-dev.json') as data_file:
	data = json.load(data_file)
	it = iter(sorted(data.items()))
	#print(next(it))
	with open('data/labled-dev.json') as labeled_file:
		labeled_data = json.load(labled_file)
		#labled_data['data'][article_index]['paragraphs'][paragraph_index]['qas']
		for article in labeled_data['data']:
			for paragraph in article['paragraph']:
				for qa in paragraph['qas']:
					if "category" in qa:
						# iterated through our sorted dev json file (which is a superset of labeled dev)
						data_tuple = next(it)
						while (data_tuple[0] != qa['id']):
							data_tuple = next(it)
						
		#for id in data:
			