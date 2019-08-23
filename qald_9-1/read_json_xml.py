import json
import pandas as pd
import nltk
import pickle
#from nltk.tag.stanford import StanfordNERTagger
import numpy as np
import sys
import os
import re
import xml.etree.ElementTree as ET

"""
creating pandas dataframe with qald_version, qald id, sentence,
"""
curr_dir = os.getcwd()
my_files = os.listdir(curr_dir)
category_df = pd.DataFrame(columns=["qald_version", "split", "question_id", "sentence_en"])
pattern_json = re.compile(r"^qald.*\.json$")
pattern_xml = re.compile(r"^qald.*\.xml$")

lines_seen = set()

for file in my_files:
	if re.match(pattern_json, file):
		competition_name = os.path.splitext(file)[0]
		qald_version = re.split('-|_', competition_name)
		split = qald_version[2]
		qald_version = qald_version[0]+'-'+qald_version[1]
		dict_multilingual_question = json.load(open(file))
		for item_obj in dict_multilingual_question["questions"]:
			for lang_obj in item_obj["question"]:
				if lang_obj["language"] == "en":
					if lang_obj["string"] not in lines_seen:
						category_df=category_df.append({'qald_version': qald_version, 'split': split, 'question_id': item_obj["id"],
													'sentence_en': lang_obj["string"]}, ignore_index=True).fillna("tbd")
						lines_seen.add(lang_obj["string"])

	elif re.match(pattern_xml, file):
		competition_name = os.path.splitext(file)[0]
		qald_version = re.split('-|_', competition_name)
		for split_type in qald_version[2:]:
			if re.match(r"test", split_type):
				split = split_type
				break
			elif re.match(r"train", split_type):
				split = split_type
				break

		qald_version = qald_version[0]+'-'+qald_version[1]

		tree = ET.parse(file)
		root = tree.getroot()
		for question in root:
			if (len(question.findall("string")) ==1):
				for lang_obj in question.findall("string"):
					if lang_obj.text not in lines_seen:
						category_df = category_df.append({'qald_version': qald_version, 'split': split, 'question_id': question.get('id'),
					 'sentence_en': lang_obj.text}, ignore_index=True).fillna("tbd")
						lines_seen.add(lang_obj.text)

			else:
				for lang_obj in question.findall("string"):
					if lang_obj.get('lang') == "en":
						if lang_obj.text not in lines_seen:
							category_df=category_df.append({'qald_version': qald_version, 'split': split, 'question_id': question.get('id'),
													'sentence_en': lang_obj.text}, ignore_index=True).fillna("tbd")
							lines_seen.add(lang_obj.text)

category_df.to_csv(os.path.join(curr_dir, "qald_combined.csv"), index=False)
# category_df.to_csv(os.path.join(curr_dir, "qald_combined_xml.csv"), index=False)
# print(category_df)
# # pickle_handle = open("pickle_df_train_raw", "wb")
# pickle_handle = open("pickle_df_test_raw", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()

