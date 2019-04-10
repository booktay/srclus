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
from pythainlp.tokenize import word_tokenize
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
501 : Replace url Error
502 : Filter th eng Error
503 : Remove stop word Error
--- 6XX Series
600 : OK
601 : Word tokenize Error
602 : POS Error
'''


# Init Tokenize class
class Tokenize:
    # Init
    def __init__(self):
        # Data from 1 thread
        # self.data = data

        # Stopwords
        self.stopwords = Stopwords()
        self.stopwords_thai, status_th = self.stopwords.languages("thai")
        self.stopwords_eng, status_eng = self.stopwords.languages("eng")

        # Custom words
        self.custom_words = Customwords()
        self.custom_words_tokenize, status_tok = self.custom_words.target("tokenize")
        self.custom_words_stopwords, status_tok = self.custom_words.target("stopwords")

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
            text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r'  ', data)
            return text, 500
        else:
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
            text = re.sub(r'[^a-zA-Z0-9ก-๙\s]+', r' ', data)
            # text = re.sub(r'([#@._%)\-\s])\1+', r'\1', text)
            # text = re.sub(r'([#@._\-])(\s)', r'\1', text)
            # TEXT = re.sub(r'(\d+)(\s)([%])', r'\2', TEXT)
            # text = re.sub(r'\s(\d+[\.)]?\d*)\s', r' ', text)
            # TEXT = re.sub(r'([!-/:-@[-`{-~])\1{1,}', r'\1', data)
            text = re.sub(r'(\s)\1+', r' ', text)
            # text = re.sub(r'([a-zA-Zก-ฮ])\1{3,}', r'\1\1', text)
            text = text.lower()
            return text, 500
        else:
            return "", 502

    '''                                                                                                                  
    Remove stopwords                                                                                                         
    ---------------- Input ---------------                                                                               
    data = ""                                                                                                            
    --------------- Output ---------------                                                                               
    str(data), int(statuscode)                                                                                           
    '''
    def removestopword(self, data=[]):
        if data == "":
            return "", 503

        text = [word for word in data if len(word) > 1 and word not in self.custom_words_stopwords]
        text = [word for word in text if word not in self.stopwords_eng and word not in self.stopwords_thai]
        return text, 500

    '''                                                                                                                  
    Tokenize word by PyThaiNLP 
    use Newmm algorithm    
    -----------
    Noun Classifier by POS Tagger
    use Orchid corpus                                                                          
    ---------------- Input ---------------                                                                               
    data = ""                                                                                                            
    --------------- Output ---------------                                                                               
    str(data), int(statuscode)                                                                                           
    '''
    def run(self, data=""):
        tokenwords_thai, tokenwords_eng = [], []

        # Wordcut
        try:
            tokenword = word_tokenize(data, engine='newmm', whitespaces=False)
            tokenword = set(tokenword)
            for word in tokenword:
                if is_thai(word, check_all=True)['thai'] > 0:
                    tokenwords_thai.append(word.replace(' ', ''))
                else:
                    tokenwords_eng.append(word.replace(' ', ''))
        except RuntimeError:
            return [], 601

        # POS Tag
        try:
            poswordsthai = thai_tag(tokenwords_thai, engine='artagger', corpus='orchid')
            poswordsthai_noun = [item[0] for item in poswordsthai if (item[1] == "NCMN" and item[0])]
            poswordseng = eng_tag(tokenwords_eng)
            poswordseng_noun = [item[0] for item in poswordseng if (item[1] not in ["IN"]and item[0])]
            poswords_noun = poswordsthai_noun + poswordseng_noun
        except RuntimeError:
            return [], 602
        return poswords_noun, 600
