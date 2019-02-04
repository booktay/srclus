#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/word2vec module

# Import Basic Module
import collections, time, json, os
import numpy as np
import tensorflow as tf

class word2vec:
    def __init__(self, data=[]):
        self.WORDSALL = data

    def getRawdata(self):
        return self.WORDSALL

    def getVocabulary(self):
        words = []
        for word in self.WORDSALL:
            words += word
        return set(words)

    def makeOnehot(self):
        word2int = {}
        int2word = {}
        vocab_size = len(words)

        for i,word in enumerate(words):
            word2int[word] = i
            int2word[i] = word
