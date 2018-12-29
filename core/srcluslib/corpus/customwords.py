#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: corpus/customwords module

# General Module
import os, json

class customwords:
    def __init__(self):
        self.CUSTOMWORDS = self.importCustomwords()
        self.LANGUAGES = self.CUSTOMWORDS.keys()

    def importCustomwords(self, filename="customwords"):
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
            return self.CUSTOMWORDS[language]

if __name__ == "__main__":
    customwords = customwords()
    print(customwords.languages("thai"))