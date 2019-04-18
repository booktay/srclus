#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/tfidf module

# General Module
import os
import json

# TF-IDF Module
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


# Init TF-IDF class
class TFIDF:
    def __init__(self, data=[]):
        self.WORD_TOKEN_ALLTHREAD = sorted(data)
        self.tfidf = TfidfVectorizer(analyzer='word', tokenizer=self.tfidftemp, preprocessor=self.tfidftemp, token_pattern=None)  
        # self.tfidf = TfidfVectorizer(tokenizer=lambda x : x.split(" "), min_df=1, max_df=1)

    @staticmethod
    def tfidftemp(doc):
        return doc

    def getRawdata(self):
        return self.WORD_TOKEN_ALLTHREAD

    def weightTfIdf(self):
        WORD = self.tfidf.fit_transform(self.WORD_TOKEN_ALLTHREAD)
        print("[Process] fit transform and weight all words")
        return WORD

    def getIDF(self):
        return self.tfidf.idf_

    def getVocabulary(self):
        print("[Process] Get Vocabulary")
        return self.tfidf.vocabulary_

    def getFeature(self):
        print("[Process] Get Features")
        return self.tfidf.get_feature_names()
    
    def getRank(self, response, feature_names):
        # doc_size = 1
        doc_size = len(self.WORD_TOKEN_ALLTHREAD)
        del self.WORD_TOKEN_ALLTHREAD
        print("[Start] Get Rank of Words")
        WORD_TARGET_ALL = []
        for doc in range(doc_size):
            feature_index = response[doc, :].nonzero()[1]
            # words_thread = sorted([[feature_names[x],response[doc, x]] for x in feature_index])
            words_thread = [feature_names[x] for x in feature_index if response[doc, x] >= 0.1]
            WORD_TARGET_ALL.append(words_thread) # [:10]
            if doc % 1000 == 0 : print("[Process] Complete " + str(doc) + " threads")
        print("[Complete] Get Rank of Words")
        return WORD_TARGET_ALL, 600
