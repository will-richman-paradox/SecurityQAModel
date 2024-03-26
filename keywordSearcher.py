import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy

nlp = spacy.load('en_core_web_sm')


def extract_keywords(list):

    for question in list:
        words = word_tokenize(question)

        stop_words = set(stopwords.words('english'))
        keywords = [word for word in words if word.lower() not in stop_words]


