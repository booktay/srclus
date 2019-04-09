#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: corpus/stopwords module

# General Module
import os
import sys
import json

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
        self.words, status = self.iorq.readjson(filepath="corpus_datas_path", filename="stopwords.json")
        self.iorq.print(self.words)
    
    # '''
    # Make a Stopwords corpus file
    # ---------------- Input ---------------
    # filepath = "../datas"
    # filename = "data.json"
    # '''
    # def makeCorpus(self, languages=["thai", "eng"], filename="temp.json"):
    #     data = {}
    #     for n in languages:
    #         if words and languages[n] in words:
    #             data[languages[n]] = sorted(set(words[languages[n]]))
    #
    #     with open(filename + ".json", 'x', encoding="utf-8") as data:
    #         json.dump(data, data, ensure_ascii=False, indent=2)

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


if __name__ == "__main__":
    stopwords = Stopwords()
    # iorq = IORQ()
    # iorq.print(stopwords.languages("thai"))
