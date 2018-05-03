import json
from collections import Counter
import re
import string 
import csv

categories_correct = Counter()
categories_wrong = Counter()
reasoning_correct = Counter()
reasoning_wrong = Counter()


def labeled_analyzer():
	"""equires correct/incorrect to be labeled"""
	with open('data/labeled-dev.json') as labeled_file:
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
				
def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))

def exact_match_score(prediction, ground_truth):
    return (normalize_answer(prediction) == normalize_answer(ground_truth))
	
def is_ground_truth(prediction, ground_truths):
	"""This function compares the prediction answer with all the ground truth answers, using the EM score for correctness"""
	for ground_truth in ground_truths:
		if exact_match_score(prediction, ground_truth):
			return True
	return False
						
def auto_analyzer():
	"""compares the model predictions with the ground truth using the EM evaluation for the SQUAD dataset"""

		#print(next(it))
	with open('data/labeled-dev.json') as labeled_file:
		labeled_data = json.load(labeled_file)
		#labled_data['data'][article_index]['paragraphs'][paragraph_index]['qas']
		for article in labeled_data['data']:
			for paragraph in article['paragraphs']:
				for qa in paragraph['qas']:
					if "category" in qa:
						# iterated through the json file with our model's sorted predictios (which is a superset of labeled dev)
						#prediction_tuple = next(it)
						#while (prediction_tuple[0] != qa['id']):
						#	prediction_tuple = next(it)
						#print(prediction_tuple)
						#print(qa['id'])
						prediction = ""
						with open('data/sorted-ensemble.json') as data_file:
							data = json.load(data_file)
							for id in data:
								if id == qa['id']:
									prediction = data[id]
						# ground truths for this particular question
						ground_truths = map(lambda x: x['text'], qa['answers'])
						#prediction = prediction_tuple[1]
						if is_ground_truth(prediction, ground_truths):
							categories_correct[qa['category']] += 1
							# for item in list
							if 'reasoning' in qa:
								for reason in qa['reasoning']:
									reasoning_correct[reason] += 1
						else:
							categories_wrong[qa['category']] += 1
							if 'reasoning' in qa:
								for reason in qa['reasoning']:
									reasoning_wrong[reason] += 1
		#for id in data:
	print(categories_correct)
	print(categories_wrong)
	print(reasoning_correct)
	print(reasoning_wrong)
	with open('out/bidaf-error.csv', 'w') as csv_file:
		writer=csv.writer(csv_file)
		 
		writer.writerow(categories_correct.keys())
		writer.writerow(categories_correct.values())
		writer.writerow(categories_wrong.keys())
		writer.writerow(categories_wrong.values())
		
		writer.writerow(reasoning_correct.keys())
		writer.writerow(reasoning_correct.values())
		writer.writerow(reasoning_wrong.keys())
		writer.writerow(reasoning_wrong.values())

#labeled_analyzer()
auto_analyzer()