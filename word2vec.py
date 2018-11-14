# Import Basic Module
import collections
import time
import json
import os
import numpy as np
import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords

class word2vec:
    def __init__(self, data=[]):
        self.WORD_TOKEN_ALLTHREAD = data
        self.TIMENOW = time.strftime("%Y%m%d%H%M")
        self.WORD_ALL = []
        self.tfidf = TfidfVectorizer(tokenizer=lambda x: x.split(), min_df=1)

    def cleanWord(self):
        stop_eng_words = set(stopwords.words('english'))
        for words in self.WORD_TOKEN_ALLTHREAD:
            print(words)
            words = [x for x in words if x not in stop_eng_words]
            print(words)
            print("*"*40)

    def weightTfIdf(self):
        self.cleanWord()
        WORD = self.tfidf.fit_transform(self.WORD_TOKEN_ALLTHREAD)
        self.WORD_ALL =  WORD
    
    def getWord(self):
        return self.WORD_ALL

    def getVocabulary(self):
        return self.tfidf.vocabulary_

    def getFeature(self):
        return self.tfidf.get_feature_names()
    
    def getScore(self):
        response = self.WORD_ALL
        # data = []
        for col in response.nonzero()[1]:
            if response[0, col] < 0.05 and response[0, col] > 0.03:
                print(self.tfidf.get_feature_names()[col], response[0, col])

    def buildDataset(self, WORDS):
        VOCABULARY_SIZE = len(WORDS)
        VOCABULARY_TOP_COUNT = [['UNK', -1]]
        VOCABULARY_TOP_COUNT.extend(collections.Counter(
            WORDS).most_common(VOCABULARY_SIZE - 1))
        DATASET = dict()
        for word, _ in VOCABULARY_TOP_COUNT:
            DATASET[word] = len(DATASET)
        DATA = list()
        UNKNOWN_COUNT = 0
        for word in WORDS:
            if word in DATASET:
                index = DATASET[word]
            else:
                index = 0  # DATASET['UNK']
                UNKNOWN_COUNT += 1
            DATA.append(index)
        VOCABULARY_TOP_COUNT[0][1] = UNKNOWN_COUNT
        REVERSE_DATASET = dict(zip(DATASET.values(), DATASET.keys()))
        return DATA, VOCABULARY_TOP_COUNT, DATASET, REVERSE_DATASET

    def generateBatch(self, BATCH_SIZE, SKIPS_NUM, SKIP_WINDOW, DATA, DATA_INDEX):
        assert BATCH_SIZE % SKIPS_NUM == 0
        assert SKIPS_NUM <= 2 * SKIP_WINDOW
        BATCH = np.ndarray(shape=(BATCH_SIZE), dtype=np.int32)
        LABELS = np.ndarray(shape=(BATCH_SIZE, 1), dtype=np.int32)
        SPAN = 2 * SKIP_WINDOW + 1
        BUFFER = collections.deque(maxlen=SPAN)
        for _ in range(SPAN):
            BUFFER.append(DATA[DATA_INDEX])
            DATA_INDEX = (DATA_INDEX + 1) % len(DATA)
        for i in range(BATCH_SIZE // SKIPS_NUM):
            TARGET = SKIP_WINDOW
            TARGETS_TO_AVOID = [SKIP_WINDOW]
            for j in range(SKIPS_NUM):
                while TARGET in TARGETS_TO_AVOID:
                    TARGET = random.randint(0, SPAN - 1)
                TARGETS_TO_AVOID.append(TARGET)
                BATCH[i * SKIPS_NUM + j] = BUFFER[SKIP_WINDOW]
                LABELS[i * SKIPS_NUM + j, 0] = BUFFER[TARGET]
            BUFFER.append(DATA[DATA_INDEX])
            DATA_INDEX = (DATA_INDEX + 1) % len(DATA)
        DATA_INDEX = (DATA_INDEX + len(DATA) - SPAN) % len(DATA)
        return BATCH, LABELS, DATA_INDEX
