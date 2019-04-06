#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: corpus/stopwords module

# General Module
import os, json, sys

# My Module
utility_path = os.path.join('..', '..', 'srcluslib')
sys.path.append(utility_path)
print(sys.path)
from srcluslib.utility.iorq import IORQ
iorq = IORQ()

'''
------------- Statuscode -------------
-- 4XX Series
400 : OK
401 : URL not response
'''

# Init Stopwords class
class Stopwords:
    '''
    Init
    '''
    def __init__(self):
        iorq.print("AAA")
        pass
        # self.STOPWORDS, self.STATUS = self.importStopwords()
        # self.LANGUAGES = self.STOPWORDS.keys() if self.STOPWORDS else None
    
    '''
    Read Json file 
    ---------------- Input ---------------
    filepath = "../datas"
    filename = "data.json"
    --------------- Output ---------------
    list(data), int(statuscode)
    '''
#     def generateStopwordsCorpus(self, languages=["thai", "eng"], words=None, filename = "temp"):
#         DATA = {}
#         for n in languages:
#             if words and languages[n] in words: 
#                 DATA[languages[n]] = sorted(set(words[languages[n]]))
#         filepath = filename + ".json"
#         with open(filepath , 'x', encoding="utf-8") as data:
#             json.dump(DATA, data, ensure_ascii=False, indent=2)

#     def importStopwords(self, filename="stopwords"):
#         # filepath = os.path.join(".", filename + ".json")
#         filepath = os.path.join("srcluslib/corpus", filename + ".json")
#         if os.path.exists(filepath):
#             words = open(filepath, 'r', encoding="utf-8")
#             return json.load(words),200
#         else: 
#             print(f'[Error] %s file not found' % filepath)
#             return None,201

#     def languages(self, language=None):
#         if self.LANGUAGES:
#             if language in self.LANGUAGES:
#                 return self.STOPWORDS[language], 200
#             else:
#                 print(f'[Error] Please choose a language [%s]' % ','.join(x for x in self.LANGUAGES))
#                 return None, 202
#         return None,201

if __name__ == "__main__":
    stopwords = Stopwords()
#     print(stopwords.languages("thai"))
