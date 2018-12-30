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
        customdict = self.customwords.target(customtype="tokenize")
        words = [word.replace(' ', '') for word in deepcut.tokenize(self.DATA, custom_dict=customdict) if word not in [' ','']]
        # words = set(words)
        words = pos_tag(words, engine='artagger', corpus='orchid')
        words = [item[0] for item in words if (item[1] == "NCMN" and (item[0] and not item[0].isnumeric()))]
        return set(words)


if __name__ == "__main__":
    pass