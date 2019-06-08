import json
import nltk

from helper_fn import sentence_preprocessing

dict_multilingual_question = json.load(open("qald-9-train-multilingual.json"))
# english_question = dict_multilingual_question.questions.question.language["en"]

# print(english_question)
count = 0
english_dict = {}
for item_obj in dict_multilingual_question["questions"]:
    # print(item)
    for lang_obj in item_obj["question"]:
        if lang_obj["language"] == "en":
            # print(lang_obj["string"])
            sentence = sentence_preprocessing(lang_obj["string"])
            print(sentence)
            count += 1
# print(count)

