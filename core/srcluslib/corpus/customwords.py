#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: corpus/customwords module

# General Module
import os, json

class customwords:
    def __init__(self):
        self.CUSTOMWORDS, self.STATUS = self.importCustomwords()
        self.TARGET = None
        if self.CUSTOMWORDS : self.TARGET = self.CUSTOMWORDS.keys()

    def importCustomwords(self, filename="customwords"):
        filepath = os.path.join("srcluslib/corpus", filename + ".json")
        if os.path.exists(filepath):
            words = open(filepath, 'r', encoding="utf-8")
            return json.load(words), 100
        else: 
            print(f'[Error] %s file not found' % filepath)
            return None, 101

    def target(self, customtype=None):
        if self.TARGET:
            if customtype in self.TARGET:
                return self.CUSTOMWORDS[customtype],100
            else:
                print(f'[Error] Please choose a type [%s]' % ','.join(x for x in self.TARGET))
                return [],103
        return None, 102

if __name__ == "__main__":
    customwords = customwords()
    print(customwords.target(customtype="tokenize"))