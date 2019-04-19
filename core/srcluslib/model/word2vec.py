#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/word2vec module

# General Module
import collections
import time
import json
import os

# Model Module
import numpy as np
# import tensorflow as tf
from gensim.models import Word2Vec
# from gensim.models.word2vec import LineSentence
import multiprocessing


# Init Word2Vec class
class W2V:
    def __init__(self, data=[], resultpath=""):
        self.WORDSALL = data
        self.RESULTPATH = resultpath

    def getRawdata(self):
        return self.WORDSALL

    def getVocabulary(self):
        words = []
        for word in self.WORDSALL:
            words += word
        return set(words)

    def euclideandist(self, vec1, vec2):
        return np.sqrt(np.sum((vec1-vec2)**2))

    def findclosest(self, word_index, vectors):
        min_dist = 10000  # to act like positive infinity
        min_index = -1
        query_vector = vectors[word_index]
        for index, vector in enumerate(vectors):
            if self.euclideandist(vector, query_vector) < min_dist and not np.array_equal(vector, query_vector):
                min_dist = self.euclideandist(vector, query_vector)
                min_index = index
        return min_index

    def makeGensim(self, document):
        model = Word2Vec(document, size=400, window=5, min_count=5, workers=multiprocessing.cpu_count())
        model.train(document, total_examples=len(document), epochs=10)
        # trim unneeded model memory = use(much) less RAM
        #model.init_sims(replace=True)
        modelpath = os.path.join(self.RESULTPATH, "vocab.model")
        model.save(modelpath)
        # model.save_word2vec_format("word.vector", binary=False)
        print("[Save] Model and Vector")

