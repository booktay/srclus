#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/preprocess module

# General Module
import os, re
# My Module
from ..corpus.stopwords import stopwords
from ..corpus.customwords import customwords

class preprocess:
    def __init__(self):
        self.stopwords = stopwords()
        self.customwords = customwords()
    
    def replaceURL(self, data=""):
        TEXT = re.sub(r'([^@])(\[[a-z]*\][ ]?)?(http[s]?://)?([^ ][a-zก-ฮะ-๙0-9]+[.][a-zก-ฮะ-๙0-9]+([/&?.=\-\w]+)?)([ ]?\[/[a-z]*\])?([ ])?', r' URLLINK ', data)
        return TEXT

    def filterOnlyTHENG(self, data=""):
        customstopword = self.customwords.target(customtype="stopwords")
        TEXT = re.sub(r'[^!-~ก-๙\s]+', r'', data)
        TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
        TEXT = re.sub(r'([^a-zA-Zก-ฮ1-9๐-๙])\1{1,}', r'\1', TEXT)
        for word in customstopword:
            TEXT = re.sub(r'(word)\1{1,}', "\1", TEXT)
        return TEXT

    def removeSpecialcharacter(self, data=""):
        TEXT = re.sub(r'[^A-Za-zก-ฮะ-๙0-9\s]+', r'', data)
        TEXT = re.sub(r'[ๆ]+', r'', TEXT)
        TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
        return TEXT

    def detectNumber(self, data=""):
        TEXT = re.sub(r'(\s)?[0-9]+(\s)?', r'', data)
        TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
        return TEXT

    def removeStopword(self, data=[]):
        stopwordthai = self.stopwords.languages("thai")
        stopwordeng = self.stopwords.languages("eng")
        customstopword = self.customwords.target(customtype="stopwords")
        text = data
        if stopwordeng:
            text = [word for word in data if word not in stopwordeng]
        if stopwordthai:
            text = [word for word in data if word not in stopwordthai]
        if customstopword:
            text = [word for word in data if word not in customstopword]
        return text

if __name__ == "__main__":
    pass