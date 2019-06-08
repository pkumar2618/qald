import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def sentence_preprocessing(sentence):
    sentence = nltk.word_tokenize(sentence)
    sentence = nltk.pos_tag(sentence)
    return sentence