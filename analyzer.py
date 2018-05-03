import json
from collections import Counter
categories_correct = Counter()
categories_wrong = Counter()
reasoning_correct = Counter()
reasoning_wrong = Counter()


def labeled_analyzer():
	# requires correct/incorrect to be labeled
	with open('data/labled-dev.json') as labeled_file:
		labeled_data = json.load(labeled_file)
		#labled_data['data'][article_index]['paragraphs'][paragraph_index]['qas']
		for article in labeled_data['data']:
			for paragraph in article['paragraphs']:
				for qa in paragraph['qas']:
					if 'result' in qa:
						# iterated through our sorted dev json file (which is a superset of labeled dev)
						if qa['result'] == 'correct':
							categories_correct[qa['category']] += 1
							# for item in list
							for reason in qa['reasoning']:
								reasoning_correct[reason] += 1
						elif qa['result'] == 'wrong':
							categories_wrong[qa['category']] += 1
							for reason in qa['reasoning']:
								reasoning_wrong[reason] += 1
	print(categories_correct)
	print(categories_wrong)
	print(reasoning_correct)
	print(reasoning_wrong)
						
def auto_analyzer():
	# TODO: link with official evaluator to figure out correct/incorrect labels
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
		
labeled_analyzer()