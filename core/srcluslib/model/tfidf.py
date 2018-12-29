#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/tfidf module

# Import Basic Module
import json, os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class tfidf:
    def __init__(self, data=[]):
        self.WORD_TOKEN_ALLTHREAD = data
        self.tfidf = TfidfVectorizer(tokenizer=lambda x: x.split(), min_df=0.1, max_df=1)

    def weightTfIdf(self):
        WORD = self.tfidf.fit_transform(self.WORD_TOKEN_ALLTHREAD)
        print("[Process] Get weight of words")
        return WORD

    def getIDF(self):
        return self.tfidf.idf_

    def getVocabulary(self):
        print("[Process] Get Vocabulary")
        return self.tfidf.vocabulary_

    def getFeature(self):
        print("[Process] Get Features")
        return self.tfidf.get_feature_names()
    
    def getRank(self):
        response = self.weightTfIdf()
        feature_names = self.getFeature()
        # doc_size = 1
        doc_size = len(self.WORD_TOKEN_ALLTHREAD)
        WORD_TARGET_ALL = []
        for doc in range(doc_size):
            feature_index = response[doc, :].nonzero()[1]
            TARGET = sorted([[response[doc, x],x] for x in feature_index])
            WORD_TARGET_ALL.append([[feature_names[x],score] for score, x in TARGET])
        print("[Process] Get Rank of Words")
        return WORD_TARGET_ALL