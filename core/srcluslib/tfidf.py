#!/usr/bin/env python
# coding: utf-8
# -------------------------
# Siwanont Sittinam
# lib/Managing Model
# -------------------------

# Import Basic Module
import time, json, os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class srclustfidf:
    def __init__(self, data=[]):
        self.WORD_TOKEN_ALLTHREAD = data
        self.TIME = time.strftime("%Y%m%d%H%M")
        self.tfidf = TfidfVectorizer(tokenizer=lambda x: x.split())

    def getWordAll(self):
        return self.WORD_TOKEN_ALLTHREAD

    def weightTfIdf(self):
        WORD = self.tfidf.fit_transform(self.WORD_TOKEN_ALLTHREAD)
        print("[TF-IDF] Get words weight by tf-idf")
        return WORD

    def getVocabulary(self):
        print("[TF-IDF] Get Vocabulary")
        return self.tfidf.vocabulary_

    def getFeature(self):
        print("[TF-IDF] Get Features")
        return self.tfidf.get_feature_names()
    
    def getOnlyRankallThread(self):
        response = self.weightTfIdf()
        feature_names = self.getFeature()
        # doc_size = 1
        doc_size = len(self.WORD_TOKEN_ALLTHREAD)
        WORD_TARGET_ALL = []
        for doc in range(doc_size):
            feature_index = response[doc, :].nonzero()[1]
            TARGET = sorted([[response[doc, x],x] for x in feature_index])[-10:]
            WORD_TARGET_ALL.append([feature_names[x] for score, x in TARGET])
        print("[TF-IDF] Get Rank Result Words")
        return WORD_TARGET_ALL
    
    def createFile(self, DATA=[], PATH="", NAME=""):
        print("[Create] " + NAME + "." + self.TIME + " file")
        if not os.path.exists(PATH):
            os.mkdir(PATH)
        PATHFILE = os.path.join(PATH, NAME + "." + self.TIME + ".json")
        access = 'x' if not os.path.exists(PATHFILE) else 'w'
        with open(PATHFILE, mode=access, encoding='utf-8') as data:
            json.dump(DATA, data, ensure_ascii=False, indent=2)
            print("[Success] " + NAME + "." + self.TIME + " file")