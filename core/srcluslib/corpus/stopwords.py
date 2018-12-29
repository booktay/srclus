#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: corpus/stopwords module

# General Module
import os, json

class stopwords:
    def __init__(self):
        self.STOPWORDS = self.importStopwords()
        self.LANGUAGES = self.STOPWORDS.keys()
    
    def generateStopwordsCorpus(self, languages=["thai", "eng"], words=None, filename = "temp"):
        DATA = {}
        for n in languages:
            if words and languages[n] in words: 
                DATA[languages[n]] = sorted(set(words[languages[n]]))
        filepath = filename + ".json"
        with open(filepath , 'x', encoding="utf-8") as data:
            json.dump(DATA, data, ensure_ascii=False, indent=2)

    def importStopwords(self, filename="stopwords"):
        filepath = filename + ".json"
        if os.path.exists(filepath):
            words = open(filepath, 'r', encoding="utf-8")
            return json.load(words)
        else: 
            print(f'[Error] %s file not found' % filepath)
            return None

    def languages(self, language=None):
        if not self.LANGUAGES:
            print(f'[Error] Please choose a language [%s]' % ','.join(x for x in self.LANGUAGES))
        else:
            return self.STOPWORDS[language]

if __name__ == "__main__":
    stopwords = stopwords()
    print(stopwords.languages("eng"))