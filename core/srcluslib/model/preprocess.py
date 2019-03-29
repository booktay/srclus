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
        if data != "":
            TEXT = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r'  ', data)
            return TEXT, 500
        else:
            print("[Error] No Operation in replaceURL function")
            return "", 501

    def filterTHENG(self, data=""):
        customstopword, status = self.customwords.target(customtype="stopwords")
        if data != "" and status == 100:
            TEXT = re.sub(r'[^a-zA-Z0-9ก-ฮะ-ูเ-์๐-๙\s#@._%)\-]+', r' ', data)
            TEXT = re.sub(r'([#@._%)\-\s])\1{1,}', r'\1', TEXT)
            TEXT = re.sub(r'([#@._\-])(\s)', r'\1', TEXT)
            # TEXT = re.sub(r'(\d+)(\s)([%])', r'\2', TEXT)
            TEXT = re.sub(r'\s(\d+[\.)]?\d*)\s', r' ', TEXT)
            # TEXT = re.sub(r'([!-/:-@[-`{-~])\1{1,}', r'\1', data)
            # TEXT = re.sub(r'(\s)\1{1,}', r' ', TEXT)
            TEXT = re.sub(r'([a-zA-Zก-ฮ])\1{3,}', r'\1\1', TEXT)
            TEXT = TEXT.lower()
            return TEXT, 500
        else :
            print("[Error] No operation in filterOnlyTHENG function")
            return "", 502

    def removeStopword(self, data=[]):
        if data == "":
            print("[Error] No Operation in removeStopword function")
            return "", 505
        stopwordthai, statusth = self.stopwords.languages("thai")
        stopwordeng, statuseng = self.stopwords.languages("eng")
        customstopword, statuscustom = self.customwords.target(customtype="stopwords")
        text = [word for word in data if word not in stopwordeng]
        text = [word for word in text if word not in stopwordthai]
        text = [word for word in text if word not in customstopword]
        text = [word for word in text if len(word) > 1]
        return text, 500

if __name__ == "__main__":
    preprocess = preprocess()
    