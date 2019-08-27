import json
import pandas as pd
import nltk
import pickle
import requests
from ast import literal_eval
#from nltk.tag.stanford import StanfordNERTagger
import numpy as np
import sys
import os
import csv
import re
import xml.etree.ElementTree as ET

"""
creating pandas dataframe with qald_version, qald id, sentence,
"""
curr_dir = os.getcwd()
my_files = os.listdir(curr_dir)
# category_df = pd.DataFrame(columns=["qald_version", "split", "question_id", "sentence_en"])
pattern_tsv = re.compile(r"^kr2ml.*\.tsv$")

# lines_seen = set()

for file in my_files:
	if re.match(pattern_tsv, file):
		para_phrases = pd.read_csv(file, delimiter="\t")
		para_phrases.insert(2, 'ori_ans_uri', 'Not Found')
		para_phrases.insert(3, 'ori_ans_label', 'Not Found')

		para_phrases.insert(5, 'pp1_ans_uri', 'Not Found')
		para_phrases.insert(6, 'pp1_ans_label', 'Not Found')
		para_phrases.insert(7, 'pp1_ori_match', 'Not Compared')

		para_phrases.insert(9, 'pp2_ans_uri', 'Not Found')
		para_phrases.insert(10, 'pp2_ans_label', 'Not Found')
		para_phrases.insert(11, 'pp2_ori_match', 'Not Compared')

		# print("reading tsv to create dataframe")
		rows = len(para_phrases.index)
		index_number = 0
		for original, pp_1, pp_2 in zip(para_phrases["Original Question"], para_phrases["Paraphrasing 1"], para_phrases["Paraphrasing 2"]):
			url = 'http://qanswer-core1.univ-st-etienne.fr/api/qa/full'

			payload = {'question': original, 'lang': 'en', 'kb': 'wikidata'}
			r = requests.get(url, params=payload)
			json_object = r.json()
			try:
				json_answer = json_object['qaContexts'][0]
				ori_answer_uri = json_answer['uri']
				ori_answer_label = json_answer['label']
				para_phrases.at[index_number, 'ori_ans_uri'] = ori_answer_uri
				para_phrases.at[index_number, 'ori_ans_label'] = ori_answer_label
			except KeyError:
				para_phrases.at[index_number, 'ori_ans_uri'] = "key exception"
				para_phrases.at[index_number, 'ori_ans_label'] = "key exception"


			payload = {'question': pp_1, 'lang': 'en', 'kb': 'wikidata'}
			r = requests.get(url, params=payload)
			json_object = r.json()
			try:
				json_answer = json_object['qaContexts'][0]
				pp1_answer_uri = json_answer['uri']
				pp1_answer_label = json_answer['label']
				para_phrases.at[index_number, 'pp1_ans_uri'] = pp1_answer_uri
				para_phrases.at[index_number, 'pp1_ans_label'] = pp1_answer_label
			except KeyError:
				para_phrases.at[index_number, 'pp1_ans_uri'] = "key exception"
				para_phrases.at[index_number, 'pp1_ans_label'] = "key exception"

			payload = {'question': pp_2, 'lang': 'en', 'kb': 'wikidata'}
			r = requests.get(url, params=payload)
			json_object = r.json()

			try:
				json_answer = json_object['qaContexts'][0]
				pp2_answer_uri = json_answer['uri']
				pp2_answer_label = json_answer['label']
				para_phrases.at[index_number, 'pp2_ans_uri'] = pp2_answer_uri
				para_phrases.at[index_number, 'pp2_ans_label'] = pp2_answer_label
			except KeyError:
				para_phrases.at[index_number, 'pp2_ans_uri'] = "key exception"
				para_phrases.at[index_number, 'pp2_ans_label'] = "key exception"

			# compare weather the answer matches with the original answer
			if ori_answer_uri == "key exception" or pp1_answer_uri == "key exception":
				para_phrases.at[index_number, 'pp1_ori_match'] = "key exception"
			elif ori_answer_uri is None and  pp1_answer_uri is None:
				para_phrases.at[index_number, 'pp1_ori_match'] = "returned no answer"
			elif ori_answer_uri is not None and pp1_answer_uri is None:
				para_phrases.at[index_number, 'pp1_ori_match'] = 0
			elif ori_answer_uri is None and pp1_answer_uri is not None:
				para_phrases.at[index_number, 'pp1_ori_match'] = 0
			elif ori_answer_uri == pp1_answer_uri:
				para_phrases.at[index_number, 'pp1_ori_match'] = 1
			else:
				para_phrases.at[index_number, 'pp1_ori_match'] = 0

			if ori_answer_uri == "key exception" or pp2_answer_uri == "key exception":
				para_phrases.at[index_number, 'pp2_ori_match'] = "key exception"
			elif ori_answer_uri is None and pp2_answer_uri is None:
				para_phrases.at[index_number, 'pp2_ori_match'] = "returned no answer"
			elif ori_answer_uri is not None and pp2_answer_uri is None:
				para_phrases.at[index_number, 'pp2_ori_match'] = 0
			elif ori_answer_uri is None and pp2_answer_uri is not None:
				para_phrases.at[index_number, 'pp2_ori_match'] = 0
			elif ori_answer_uri == pp2_answer_uri:
				para_phrases.at[index_number, 'pp2_ori_match'] = 1
			else:
				para_phrases.at[index_number, 'pp2_ori_match'] = 0


			index_number += 1
			# print(original, pp_1, pp_2)


para_phrases.to_csv(os.path.join(curr_dir, "para_phrase_answers.tsv"), sep='\t', index=False)

# print(category_df)
# # pickle_handle = open("pickle_df_train_raw", "wb")
# pickle_handle = open("pickle_df_test_raw", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()

