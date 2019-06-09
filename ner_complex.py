import json
import pandas as pd
import nltk
import pickle
import numpy as np
from helper_fn import sentence_preprocessing, pos_complex, list_type, count_type


"""
creating pandas dataframe with qald id, sentence, pos-complex, ner-complex,
OpenIE-complex, list type(Y/N), count_type(Y/N)
"""
# dict_multilingual_question = json.load(open("qald-9-train-multilingual.json"))
# category_df = pd.DataFrame(columns=["qald_id", "sentence_en", "pos-complex(H/M/E)", "ner-complex(H/M/E)",
#                                        "OpenIE-complex(H/M/E)", "list_type(Y/N)", "count_type(Y/N)"])
#
# for item_obj in dict_multilingual_question["questions"]:
#     for lang_obj in item_obj["question"]:
#         if lang_obj["language"] == "en":
#             category_df = category_df.append({'qald_id': item_obj["id"], 'sentence_en':
#             lang_obj["string"]}, ignore_index=True).fillna("tbd")
# # print(category_df)
# pickle_handle = open("pickle_df_raw", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()


"""
determining POS complexity
pos-complex(E): when sentence has two or less NN/WP tags and 0+ not(NN) tag
pos-complex(M): when sentence has 3 NN/WP tags and 1+ not(NN and WP) tags
pos-complex(H): when sentence has 4 or more NN/WP tags and 1+ not(NN and WP) tags
"""
# pickle_handle = open("pickle_df_raw", "rb")
# category_df = pickle.load(pickle_handle)
# pickle_handle.close()
# # # print(category_df)
# category_df = category_df.set_index("qald_id", drop=False)
# for id_label in category_df.index:
#     sentence = sentence_preprocessing(category_df.at[id_label, "sentence_en"])
#     # print(sentence)
#     label_HME = pos_complex(sentence)
#     category_df.at[id_label, "pos-complex(H/M/E)"] = label_HME
#
# pickle_handle = open("pickle_df_processed", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()


"""
label sentence are 'list' type and 'count' type
"""
# pickle_handle = open("pickle_df_processed", "rb")
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
# pickle_handle = open("pickle_df_processed", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()
# print(category_df)


"""
NER Tagging
"""
pickle_handle = open("pickle_df_processed", "rb")
category_df = pickle.load(pickle_handle)
pickle_handle.close()
print(category_df)
