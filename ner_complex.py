import json
import pandas as pd
import nltk
import pickle
from helper_fn import sentence_preprocessing

# dict_multilingual_question = json.load(open("qald-9-train-multilingual.json"))
#
# ### creating pandas dataframe with qald id, sentence, pos-complex, ner-complex, OpenIE-complex, list type(Y/N), count_type(Y/N)
# category_df = pd.DataFrame(columns=["qald_id", "sentence_en", "pos-complex(H/M/E)", "ner-complex(H/M/E)",
#                                        "OpenIE-complex(H/M/E)", "list_type(Y/N)", "count_type(Y/N)"])
#
# for item_obj in dict_multilingual_question["questions"]:
#     for lang_obj in item_obj["question"]:
#         if lang_obj["language"] == "en":
#             category_df = category_df.append({'qald_id': item_obj["id"], 'sentence_en': lang_obj["string"]}, ignore_index=True).fillna(0)
#
# # print(category_df)
# pickle_handle = open("pickle_df_raw", "wb")
# pickle.dump(category_df, pickle_handle)
# pickle_handle.close()

pickle_handle = open("pickle_df_raw", "rb")
category_df = pickle.load(pickle_handle)
pickle_handle.close()
print(category_df)