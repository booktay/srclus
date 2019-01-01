#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/tokenize module

# Import NLP Module
import deepcut
from pythainlp.tag import pos_tag
import nltk
# My Module
from ..corpus.customwords import customwords

class tokenize:
    def __init__(self, data=""):
        self.DATA = data
        self.customwords = customwords()

    def run(self):
        customdict. statuscustom = self.customwords.target(customtype="tokenize")
        statusrun = 400
        # Wordcut
        try:
            words = [word.replace(' ', '') for word in deepcut.tokenize(self.DATA, custom_dict=customdict) if word not in [' ','']]
        except:
            print("[Error] DEEPCUT Function")
            words = self.DATA
            statusrun = 401
        
        words = set(words)

        # Part of speech
        try:
            words = pos_tag(words, engine='artagger', corpus='orchid')
            words = [item[0] for item in words if (item[1] == "NCMN" and (item[0] and not item[0].isnumeric()))]
        except:
            print("[Error] POS_TAG Function")
            words = words
            statusrun = 402

        return set(words), statusrun


if __name__ == "__main__":
    pass