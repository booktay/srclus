#!/usr/bin/env python
# coding: utf-8
# -------------------------
# Siwanont Sittinam
# lib/Rank tfidf
# -------------------------

# Import Basic Module
import json, os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class srclustfidf:
    def __init__(self, data=[]):
        self.WORD_TOKEN_ALLTHREAD = data
        self.tfidf = TfidfVectorizer(tokenizer=lambda x: x.split(), min_df=0.1, max_df=1)

    def getWordAll(self):
        return self.WORD_TOKEN_ALLTHREAD

    def weightTfIdf(self):
        WORD = self.tfidf.fit_transform(self.WORD_TOKEN_ALLTHREAD)
        print("[TF-IDF] Get words weight by tf-idf")
        return WORD
    
    def getIDF(self):
        return self.tfidf.idf_

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
            TARGET = sorted([[response[doc, x],x] for x in feature_index])
            WORD_TARGET_ALL.append([[feature_names[x],score] for score, x in TARGET])
        print("[TF-IDF] Get Rank Result Words")
        return WORD_TARGET_ALL
    
    def createFile(self, DATA=[], PATH="", NAME=""):
        # print("[Create] " + NAME + ".json")
        if not os.path.exists(PATH):
            os.mkdir(PATH)
        PATHFILE = os.path.join(PATH, NAME + ".json")
        access = 'x' if not os.path.exists(PATHFILE) else 'w'
        with open(PATHFILE, mode=access, encoding='utf-8') as data:
            json.dump(DATA, data, ensure_ascii=False, indent=2)
            print("[Success] " + NAME + ".json")