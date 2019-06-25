import json
import pandas as pd
import nltk
import pickle
from nltk.tag.stanford import StanfordNERTagger
import numpy as np
from helper_fn import sentence_preprocessing, pos_complex, noun_count, list_type, count_type, ner_complex


"""
creating pandas dataframe with qald id, sentence, pos-complex, ner-complex,
OpenIE-complex, list type(Y/N), count_type(Y/N)
"""
# # dict_multilingual_question = json.load(open("qald-9-train-multilingual.json"))
# dict_multilingual_question = json.load(open("qald-9-test-multilingual.json"))
# category_df = pd.DataFrame(columns=["qald_id", "sentence_en",
#                                     "pos-tags", "noun_count", "pos-complex(H/M/E)",
#                                     "ner-tags", "entity_count", "ner-complex(H/M/E)",
#                                     "list_type(Y/N)", "count_type(Y/N)"])
#
# for item_obj in dict_multilingual_question["questions"]:
#     for lang_obj in item_obj["question"]:
#         if lang_obj["language"] == "en":
#             category_df = category_df.append({'qald_id': item_obj["id"], 'sentence_en':
#             lang_obj["string"]}, ignore_index=True).fillna("tbd")
# # print(category_df)
# # pickle_handle = open("pickle_df_train_raw", "wb")
# pickle_handle = open("pickle_df_test_raw", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()


"""
determining POS complexity
pos-complex(E): when sentence has two or less NN/WP tags and 0+ not(NN) tag
pos-complex(M): when sentence has 3 NN/WP tags and 1+ not(NN and WP) tags
pos-complex(H): when sentence has 4 or more NN/WP tags and 1+ not(NN and WP) tags
"""
# # pickle_handle = open("pickle_df_train_raw", "rb")
# pickle_handle = open("pickle_df_test_raw", "rb")
# category_df = pickle.load(pickle_handle)
# pickle_handle.close()
# # # print(category_df)
# category_df = category_df.set_index("qald_id", drop=False)
# for id_label in category_df.index:
#     sentence = sentence_preprocessing(category_df.at[id_label, "sentence_en"])
#     # print(sentence)
#     tag_count_complexity = pos_complex(sentence)
#     category_df.at[id_label, "pos-tags"] = tag_count_complexity[0]
#     category_df.at[id_label, "noun_count"] = tag_count_complexity[1]
#     category_df.at[id_label, "pos-complex(H/M/E)"] = tag_count_complexity[2]
#
# # pickle_handle = open("pickle_df_train_processed", "wb")
# pickle_handle = open("pickle_df_test_processed", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()

"""
label sentence are 'list' type and 'count' type
"""
# # pickle_handle = open("pickle_df_train_processed", "rb")
# pickle_handle = open("pickle_df_test_processed", "rb")
# category_df = pickle.load(pickle_handle)
# pickle_handle.close()
# # print(category_df)
# category_df = category_df.set_index("qald_id", drop=False)
# for id_label in category_df.index:
#     sentence = sentence_preprocessing(category_df.at[id_label, "sentence_en"])
#     # print(sentence)
#     list_found = list_type(sentence)
#     category_df.at[id_label, "list_type(Y/N)"] = list_found
#     count_found = count_type(sentence)
#     category_df.at[id_label, "count_type(Y/N)"] = count_found
#
# # pickle_handle = open("pickle_df_train_processed", "wb")
# pickle_handle = open("pickle_df_test_processed", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()
# print(category_df)


"""
NER Tagging
"""
# pickle_handle = open("pickle_df_train_processed", "rb")
pickle_handle = open("pickle_df_test_processed", "rb")
category_df = pickle.load(pickle_handle)
pickle_handle.close()
# print(category_df)
#
jar = './stanford-ner.jar'
model = './english.all.3class.distsim.crf.ser.gz'

# Prepare NER tagger with english model
ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

category_df = category_df.set_index("qald_id", drop=False)
for id_label in category_df.index:
    sentence = category_df.at[id_label, "sentence_en"]

    # Tokenize: Split sentence into words
    words = nltk.word_tokenize(sentence)

    # Run NER tagger on words
    words_ner = ner_tagger.tag(words)
    # print(words_ner)

    ner_entity_complxity = ner_complex(words_ner)
    # category_df.at[id_label, "ner-tags"] = ner_entity_complxity[0]
    # category_df.at[id_label, "entity-count"] = ner_entity_complxity[1]
    # category_df.at[id_label, "ner-complex(H/M/E)"] = ner_entity_complxity[2]
    category_df.at[id_label, "sentence_entities_grayed"] = ner_entity_complxity[3]

# pickle_handle = open("pickle_df_train_processed", "wb")
pickle_handle = open("pickle_df_test_processed", "wb")
pickle.dump(category_df, pickle_handle)
pickle_handle.close()
# print(category_df)

"""
OpenIE-complex
"""
# pickle_handle = open("pickle_df_processed", "rb")
# category_df = pickle.load(pickle_handle)
# pickle_handle.close()
# # print(category_df)
