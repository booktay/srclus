#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/tokenize module

# General Module
import os
import sys
import re

# Part of speech Module
from pythainlp.tag import pos_tag as thai_tag
from nltk import pos_tag as eng_tag
# Check Thai Language Module
from pythainlp.util import is_thai
# Tokenize Module
from pythainlp.tokenize import dict_word_tokenize
# import deepcut

# My Module
sys.path.insert(0, os.path.abspath('..'))
from corpus.stopwords import Stopwords
from corpus.customwords import Customwords
from utility.iorq import IORQ


'''
------------- Statuscode -------------
-- 4XX Series
400 : OK
401 : Error
-- 5XX Series
500 : OK
501 : Replaceurl Error
502 : Filtertheng Error
503 : Removestopword Error
'''


# Init Preprocess class
class Preprocess:
    # Init
    def __init__(self):
        self.stopwords = Stopwords()
        self.custom_words = Customwords()

    '''                                                                                                                  
    Replace URL with 2 space                                                                                             
    ---------------- Input ---------------                                                                               
    data = "https://www.google.co.th"                                                                                    
    --------------- Output ---------------                                                                               
    str(data), int(statuscode)                                                                                           
    '''
    @staticmethod
    def replaceurl(data=""):
        if data != "":
            text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r' ', data)
            return text, 500
        else:
            print("[Error] No Operation in replaceurl function")
            return "", 501

    '''                                                                                                                  
    Filter words                                                                                                         
    ---------------- Input ---------------                                                                               
    data = ""                                                                                                            
    --------------- Output ---------------                                                                               
    str(data), int(statuscode)                                                                                           
    '''
    @staticmethod
    def filtertheng(data=""):
        if data != "":
            text = re.sub(r'[^a-zA-Z0-9ก-ฮะ-ูเ-์๐-๙\s#@._%)\-]+', r' ', data)
            text = re.sub(r'([#@._%)\-\s])\1+', r'\1', text)
            text = re.sub(r'([#@._\-])(\s)', r'\1', text)
            # TEXT = re.sub(r'(\d+)(\s)([%])', r'\2', TEXT)
            text = re.sub(r'\s(\d+[\.)]?\d*)\s', r' ', text)
            # TEXT = re.sub(r'([!-/:-@[-`{-~])\1{1,}', r'\1', data)
            # TEXT = re.sub(r'(\s)\1{1,}', r' ', TEXT)
            text = re.sub(r'([a-zA-Zก-ฮ])\1{3,}', r'\1\1', text)
            text = text.lower()
            return text, 500
        else:
            print("[Error] No operation in filtertheng function")
            return "", 502

    '''                                                                                                                  
    Filter words                                                                                                         
    ---------------- Input ---------------                                                                               
    data = ""                                                                                                            
    --------------- Output ---------------                                                                               
    str(data), int(statuscode)                                                                                           
    '''
    def removestopword(self, data=[]):
        if data == "":
            print("[Error] No Operation in removestopword function")
            return "", 503
        stopwordthai, statusth = self.stopwords.languages("thai")
        stopwordeng, statuseng = self.stopwords.languages("eng")
        customstopword, statuscustom = self.customwords.target(customtype="stopwords")
        text = [word for word in data if word not in stopwordeng]
        text = [word for word in text if word not in stopwordthai]
        text = [word for word in text if word not in customstopword]
        text = [word for word in text if len(word) > 1]
        return text, 500


# Init Tokenize class
class Tokenize:
    def __init__(self, data=[]):
        self.data = data
        self.custom_words = Customwords()

    # def run(self):
    #     customdict, statuscustom = self.custom_words.target(customtype="tokenize")
    #     tokenwords_thai, tokenwords_eng, statusrun = [], [], 600
    #     # Wordcut
    #     try:
    #         for word in self.DATA:
    #             if isthai(word, check_all=True)['thai'] > 0:
    #                 # tokenword = deepcut.tokenize(word, custom_dict=customdict)
    #                 tokenword = dict_word_tokenize(word,customdict, engine='newmm')
    #                 if tokenword: tokenwords_thai += [word.replace(' ', '') for word in tokenword if word not in [' ','']]
    #             else:
    #                 if not word.isdigit(): tokenwords_eng.append(word)
    #     except:
    #         print("[Error] Wordcut Function")
    #         statusrun = 601
    #     tokenwords_thai = set(tokenwords_thai)
    #     tokenwords_eng = set(tokenwords_eng)
    #     # POS Tag
    #     try:
    #         poswordsthai = thai_tag(tokenwords_thai, engine='artagger', corpus='orchid')
    #         poswordsthai_noun = [item[0] for item in poswordsthai if (item[1] == "NCMN" and item[0])]
    #
    #         poswordseng = eng_tag(tokenwords_eng)
    #         poswordseng_noun = [item[0] for item in poswordseng if (item[1] not in ["IN"]and item[0])]
    #         poswords_noun = poswordsthai_noun + poswordseng_noun
    #     except:
    #         print("[Error] POS Tag Function")
    #         poswords_noun = tokenwords_thai + tokenwords_eng
    #         statusrun = 402
    #     tokenwords = set(poswords_noun)
    #     return tokenwords, statusrun


if __name__ == "__main__":
    Tokenize(data=['Apple สวัสดี now has Mr.']).run()