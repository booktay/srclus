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
import pythainlp as ptn
import numpy as np
import tensorflow as tf
import deepcut as dc

WORD_TOKEN = []
PATH = os.path.join('data/', "word_token_allthread_201810310613" + '.json')
with open(PATH, mode='r', encoding='utf-8') as store_word:
    WORD_TOKEN_ALLTHREAD = json.load(store_word)
    for wordd in WORD_TOKEN_ALLTHREAD:
        tok = ptn.tokenize.word_tokenize(wordd, engine='deepcut', whitespaces=True)
        print(tok)