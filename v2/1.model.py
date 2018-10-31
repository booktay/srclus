#!/usr/bin/env python
# coding: utf-8

import sys
import os
import requests
import json
import time
import re
import math
import random

from six.moves import xrange
import numpy as np
import tensorflow as tf
import deepcut as dc
from sklearn.manifold import TSNE
from multiprocessing import Pool

def replaceCharinToken(WORD_TOKEN, CUSTOM_WORD):
    # print(CUSTOM_WORD)
    number = 0
    while True:
        if WORD_TOKEN[number] == ' ' or WORD_TOKEN[number] in CUSTOM_WORD:
            WORD_TOKEN.remove(WORD_TOKEN[number])
        else:
            number += 1
        if number == len(WORD_TOKEN):
            return WORD_TOKEN

def getTokenWordFromUrl(THREAD_RUN):
    # Define Variable
    BASE_PATH = "https://ptdev03.mikelab.net/kratoo/"
    THREAD_ID = 30000000 + THREAD_RUN
    URL = BASE_PATH + str(THREAD_ID)

    CUSTOM_WORD = manageCustomWord()
    # print(CUSTOM_WORD)

    # Request
    RAW_REQUEST = requests.get(URL).json()
    if (RAW_REQUEST["found"]):
        RAW_SOURCE = RAW_REQUEST["_source"]
        TOKEN_TITLE = RAW_SOURCE["title"]
        TOKEN_DESC = RAW_SOURCE["desc"]  # "comments_desc"
        WORD_UNTOKEN = replaceWord(TOKEN_TITLE + " " + TOKEN_DESC)
        WORD_TOKEN = dc.tokenize(WORD_UNTOKEN, CUSTOM_WORD)
        WORD_TOKEN = replaceCharinToken(WORD_TOKEN, CUSTOM_WORD)
        return WORD_TOKEN
    return []

def runToken(THREAD=[0,1]):
    WORD_TOKEN_ALLTHREAD = []
    for THREAD_RUN in xrange(THREAD[0], THREAD[1]):
        WORD_TOKEN = getTokenWordFromUrl(THREAD_RUN)
        WORD_TOKEN_ALLTHREAD += WORD_TOKEN
        if THREAD_RUN % 10 == 0:
            print("At Thread : " + str(THREAD_RUN))
    return WORD_TOKEN_ALLTHREAD


def buildTokenSet():
    ALL_THREAD = [[x * 10000, (x + 1) * 10000] for x in range(20)]
    # ALL_THREAD = [[x * 10, (x + 1) * 10] for x in range(10)]
    with Pool(processes=20) as pool:
        WORD_TOKEN_ALLTHREAD = pool.map(runToken, ALL_THREAD)
    return WORD_TOKEN_ALLTHREAD


def buildGraph(final_embeddings, reverse_dictionary):
    print(reverse_dictionary)
    try:
        tsne = TSNE(perplexity=50, n_components=2, init='pca', n_iter=5000, learning_rate=800)
        plot_only = 5000
        low_dim_embs = tsne.fit_transform(final_embeddings[:plot_only, :])
        labels = [reverse_dictionary[str(i)] for i in range(plot_only)]
        return low_dim_embs, labels
    except ImportError:
        print("Please install sklearn, matplotlib, and scipy to visualize embeddings.")
    return

def generateGraphdata():
    final_embeddings = loadFile('final_embeddings_201810182013')
    dataset = loadFile('dataset_201810182013')
    print("[Success] import dataset & final_embedding")
    low_dim_embs, labels = buildGraph(np.array(final_embeddings), dataset['reverse_dataset'])
    createFile({"low_dim_embs": low_dim_embs.tolist(), "labels": labels}, "plot")
    print("[Success] Subprocess plot ")

def plateProcess():
    # Process 1
    # WORD_TOKEN_ALLTHREAD = buildTokenSet()
    # WORD_TOKEN_ALLTHREAD = list(itertools.chain.from_iterable(WORD_TOKEN_ALLTHREAD))
    # print(WORD_TOKEN_ALLTHREAD)
    # createFile(WORD_TOKEN_ALLTHREAD, 'word_token_allthread')
    WORD_TOKEN_ALLTHREAD = loadFile('word_token_allthread_201810182013')
    print("[Complete] Process 1 : Token All thread")
    # Process 2
    buildModel(WORD_TOKEN_ALLTHREAD)
    print("[Complete] Process 2 : Model")

def main():
    try:
        plateProcess()
        # generateGraphdata()
    except KeyboardInterrupt:
        print("[Cancel] Ctrl-c Detect")
    finally:
        print("[Close] ")

if __name__ == '__main__':
    main()
