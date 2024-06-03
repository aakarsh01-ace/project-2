import json
import numpy as np
import random
import tensorflow as tf
import tflearn
from tensorflow.python.framework import ops
from nltk.stem.lancaster import LancasterStemmer
import nltk

nltk.download('punkt')

stemmer = LancasterStemmer()

# LOAD INTENTS
with open("data/intents.json") as file:
    data = json.load(file)


# EXTRACT DATA
words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrd = nltk.word_tokenize(pattern)
        words.extend(wrd)
        docs_x.append(wrds)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

# Stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w!="?"]
words = sorted(list(set(words)))

labels = sorted(labels)


 