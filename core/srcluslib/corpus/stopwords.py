#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: corpus/stopwords module

# General Module
import os
import sys

# My Module
sys.path.insert(0, os.path.abspath('..'))
from utility.iorq import IORQ


'''
------------- Statuscode -------------
-- 2XX Series
200 : OK
201 : Not found language
'''


# Init Stopwords class
class Stopwords:
    # Init
    def __init__(self):
        self.iorq = IORQ()
        corpus_datas_path = os.path.join("..", "..", "datas", "corpus")
        self.words, status = self.iorq.readjson(filepath=corpus_datas_path, filename="stopwords.json")
        # self.iorq.print(self.words)

    # '''
    # Request stopwords
    # ---------------- Input ---------------
    # language = "thai"
    # ---------------- Output --------------
    # list(data), int(Status code)
    # '''
    def languages(self, language=""):
        language = language.lower()
        if self.words[language]:
            return self.words[language], 200
        else:
            print(f'[Error] Please choose another language')
            return None, 201


# if __name__ == "__main__":
    # stopwords = Stopwords()
    # iorq = IORQ()
    # iorq.print(stopwords.languages("thai"))
