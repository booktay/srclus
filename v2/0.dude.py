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
import collections
import zipfile
import itertools
from six.moves import xrange
from multiprocessing import Pool

TIMENOW = time.strftime("%Y%m%d%H%M")

def createFile(DATA, NAME):
    with open(os.path.join('data/', NAME + "_" + TIMENOW + '.json'), mode='x', encoding='utf-8') as store_word:
        json.dump(DATA, store_word, ensure_ascii=False)

def manageCustomWord(OPTION='r', DATA=[]):
    with open('custom_word.json', mode='r', encoding='utf-8') as custom_word:
        CUSTOM_WORD = json.load(custom_word)
    if OPTION == 'r':
        return CUSTOM_WORD
    elif OPTION == 'w':
        with open('custom_word.json', mode='w', encoding='utf-8') as custom_word:
            CUSTOM_WORD += DATA
            json.dump(CUSTOM_WORD, custom_word, ensure_ascii=False)
    return


def getTokenWordFromUrl(THREAD_RUN):
    BASE_PATH = "https://ptdev03.mikelab.net/kratoo/"
    THREAD_ID = 30000000 + THREAD_RUN
    URL = BASE_PATH + str(THREAD_ID)

    # Request
    try :
        RAW_REQUEST = requests.get(URL).json()
    except :
        return []

    if (RAW_REQUEST["found"]):
        RAW_SOURCE = RAW_REQUEST["_source"]
        TOKEN_TITLE = RAW_SOURCE["title"]
        TOKEN_DESC = RAW_SOURCE["desc"]  # "comments_desc"
        WORD_TOKEN = TOKEN_TITLE + " " + TOKEN_DESC
        return WORD_TOKEN
    return []


def runToken(THREAD=[0, 1]):
    WORD_TOKEN_ALLTHREAD = []
    for THREAD_RUN in xrange(THREAD[0], THREAD[1]):
        WORD_TOKEN = getTokenWordFromUrl(THREAD_RUN)
        WORD_TOKEN_ALLTHREAD += WORD_TOKEN
        if THREAD_RUN % 10 == 0:
            print("At Thread : " + str(THREAD_RUN))
    return WORD_TOKEN_ALLTHREAD

def buildTokenSet():
    ALL_THREAD = [[x, x + 15000] for x in range(10**5, 2*10**5, 15000)]
    with Pool(processes=len(ALL_THREAD)) as pool:
        WORD_TOKEN_ALLTHREAD = pool.map(runToken, ALL_THREAD)
    return WORD_TOKEN_ALLTHREAD

def main():
    try:
        # Process 1
        WORD_TOKEN_ALLTHREAD = buildTokenSet()
        WORD_TOKEN_ALLTHREAD = list(itertools.chain.from_iterable(WORD_TOKEN_ALLTHREAD))
        # print(WORD_TOKEN_ALLTHREAD)
        createFile(WORD_TOKEN_ALLTHREAD, 'word_token_allthread')
    except KeyboardInterrupt:
        print("[Cancel] Ctrl-c Detect")
        createFile(WORD_TOKEN_ALLTHREAD, 'word_token_allthread')
    finally:
        print("[Close] ")


if __name__ == '__main__':
    main()
