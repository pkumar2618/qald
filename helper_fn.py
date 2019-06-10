import nltk
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
import re


def sentence_preprocessing(sentence):
    sentence = nltk.word_tokenize(sentence)
    sentence = nltk.pos_tag(sentence)
    return sentence

def pos_complex(pos_tagged_sentence):
    pattern_nn = ["NN.*", "WP"]
    pattern_nn_combined = "(" + ")|(".join(pattern_nn) + ")"
    # print(pattern)
    noun_count = 0
    other_count = 0
    for word_tag in pos_tagged_sentence:
        # noun_tag = re.search(r'(NN.*)|(WP)', word_tag[1])
        noun_tag = re.search(pattern_nn_combined, word_tag[1])
        if noun_tag:
            noun_count += 1
        else:
            other_count += 1

    if noun_count > 3 and other_count > 0:
        return "hard"
    elif noun_count == 3 and other_count > 0:
        return "medium"
    else:
        return "easy"


def list_type(sentence):
    list_count = 0
    for word_tag in sentence:
        list_found = re.search(r'\b[lL]ist\b', word_tag[0])
        if list_found:
            list_count += 1

    for i in range(len(sentence) - 3):
        if re.search(r'\b([gG]ive)|([fF]ind)\b', sentence[i][0]):
            if (re.search(r'\b(me)\b', sentence[i+1][0])) and (re.search(r'\ball\b', sentence[i+2][0])):
                list_count += 1
            elif (re.search(r'(\ball\b)', sentence[i+1][0])) and (re.search(r'\bthe\b', sentence[i+2][0])):
                list_count += 1

    if list_count >= 1:
        return "Y"
    else:
        return "N"


def count_type(sentence):
    count_count = 0
    for word_tag in sentence:
        count_found = re.search(r'\b[cC]ount[sS]*\b', word_tag[0])
        if count_found:
            count_count += 1

    if count_count >= 1:
        return "Y"
    else:
        return "N"


def ner_complex(words_ner):
    pattern_entity = ["LOCATION", "PERSON", "ORGANIZATION"]
    pattern_entity_combined = "(" + ")|(".join(pattern_entity) + ")"
    # # print(pattern)
    entity_count = 0
    for word_entity in words_ner:
        entity = re.search(pattern_entity_combined, word_entity[1])
        if entity:
            entity_count += 1

    if entity_count >= 5:
        return "hard"
    elif entity_count == 4:
        return "medium"
    else:
        return "easy"

