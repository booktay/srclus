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
            TEXT = re.sub(r'([^@])(\[[a-z]*\][ ]?)?(http[s]?://)?([^ ][a-zก-ฮะ-๙0-9]+[.][a-zก-ฮะ-๙0-9]+([/&?.=\-\w]+)?)([ ]?\[/[a-z]*\])?([ ])?', r' URLLINK ', data)
            return TEXT, 300
        else:
            print("[Error] No Operation in replaceURL function")
            return "", 301

    def filterOnlyTHENG(self, data=""):
        customstopword, status = self.customwords.target(customtype="stopwords")
        if data and status == 200:
            TEXT = re.sub(r'[^!-~ก-๙\s]+', r'', data)
            TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
            TEXT = re.sub(r'([^a-zA-Zก-ฮ1-9๐-๙])\1{1,}', r'\1', TEXT)
            for word in customstopword:
                TEXT = re.sub(r'(word)\1{1,}', "\1", TEXT)
            return TEXT, 300
        else :
            print("[Error] No operation in filterOnlyTHENG function")
            return None, 302

    def removeSpecialcharacter(self, data=""):
        if data != "":
            TEXT = re.sub(r'[^A-Za-zก-ฮะ-๙0-9\s]+', r'', data)
            TEXT = re.sub(r'[ๆ]+', r'', TEXT)
            TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
            return TEXT,300
        else:
            print("[Error] No Operation in removeSpecialcharacter function")
            return "", 303

    def detectNumber(self, data=""):
        if data != "":
            TEXT = re.sub(r'(\s)?[0-9]+(\s)?', r'', data)
            TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
            return TEXT, 300
        else:
            print("[Error] No Operation in detectNumber function")
            return "", 304

    def removeStopword(self, data=[]):
        if data != "":
            print("[Error] No Operation in removeStopword function")
            return "", 305
        stopwordthai, statusth = self.stopwords.languages("thai")
        stopwordeng, statuseng = self.stopwords.languages("eng")
        customstopword, statuscustom = self.customwords.target(customtype="stopwords")
        text = data
        if statuseng 
        if statuseng == 200 and stopwordeng:
            text = [word for word in data if word not in stopwordeng]
        if statusth == 200 and stopwordthai:
            text = [word for word in data if word not in stopwordthai]
        if statuscustom == 100 and customstopword:
            text = [word for word in data if word not in customstopword]
        return text, 300

if __name__ == "__main__":
    pass