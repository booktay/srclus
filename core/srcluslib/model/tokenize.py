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
        words, statusrun = self.DATA, 400
        # Wordcut
        try:
            tokenword = deepcut.tokenize(self.DATA, custom_dict=customdict)
            if tokenword: words = [word.replace(' ', '') for word in tokenword if word not in [' ','']]
        except:
            print("[Error] Wordcut Function")
            statusrun = 401
        words = set(words)
        # POS Tag
        try:
            poswords = pos_tag(words, engine='artagger', corpus='orchid')
            words = [item[0] for item in poswords if (item[1] == "NCMN" and item[0])]
        except:
            print("[Error] POS Tag Function")
            words = words
            statusrun = 402

        return set(words), statusrun


if __name__ == "__main__":
    pass