#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: model/tokenize module

# General Module
import os
import sys
import re

import unicodedata

# Part of speech Module
from pythainlp.tag import pos_tag as thai_tag
from nltk import pos_tag as eng_tag

# Check Thai Language Module
from pythainlp.util import isthai, num_to_thaiword, text_to_arabic_digit

# Tokenize Module
from pythainlp.tokenize import word_tokenize
# import deepcut

# My Module
# sys.path.insert(0, os.path.abspath('..'))
from ..corpus.stopwords import Stopwords
from ..corpus.customwords import Customwords
from ..utility.iorq import IORQ
iorq = IORQ()

'''
------------- Statuscode -------------
-- 4XX Series
400 : OK
401 : Error
-- 5XX Series
500 : OK
501 : Replace url Error
502 : Filter th eng Error
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
            # # Remove Another Language
            # TEXT = re.sub(r'[^!-~ก-๙\s]+', r'', TEXT)
            # # Link URL
            # TEXT = re.sub(
            #     r'(http[s]?://)?([a-zก-ฮ0-9]+[.]?[a-zก-ฮ0-9]+)[.][a-zก-ฮ]+[/&?.=\-\w]*', r'URLLINK', TEXT)
            # # Duplicate Char
            # TEXT = re.sub(r'555+|ถถถ+', 'ตลก', TEXT)
            # TEXT = re.sub(r'([a-zก-๙])\1{3,}', r'\1', TEXT)
            # TEXT = re.sub(r'([a-zก-๙])\1{2,}\s+', r'\1 ', TEXT)
            # # Time
            # TEXT = re.sub(r"(\d+)\s(ชั่วโมง|นาที|วินาที)", r"\1\2", TEXT)
            # TEXT = re.sub(r"(\d+)\s(hour|minute|second|sec[s]?)", r"\1\2", TEXT)
            # # Word Space
            # TEXT = re.sub(r"(\d+)([.)])\s([a-zก-๙]+)", r"\1\2\3", TEXT)
            # TEXT = re.sub(r"([a-zก-๙]+)\s(\d+)\s(%)", r"\1\2\3", TEXT)
            # TEXT = re.sub(r"([a-zก-๙]+)[\s\-](\d+)\s", r"\1\2 ", TEXT)
            # TEXT = re.sub(r"\s+(and|or)\s+", r"\1", TEXT)
            # TEXT = re.sub(r"\s+[0-9]+\s+", " ", TEXT)
            # # Special Char
            # TEXT = re.sub(r"[<(\{\[\\/#]+\s*(\w+)\s*[>)\}\]\\/#]+", r"\1 ", TEXT)
            # TEXT = re.sub(r'[@!-/:->\[-`{-~]+', '', TEXT)
            # TEXT = re.sub(r'[:/&?#.\-ๆ]', '', TEXT)
            # TEXT = re.sub(r'(\s)\1{1,}', r'\1', TEXT)
            # # Add Multilanguage Detect
            # TEXT = re.sub("(^[a-z]+[0-9๐-๙]*)", r"[EN][@@]\1", TEXT)
            # TEXT = re.sub("(^[ก-๐]+[0-9๐-๙]*)", r"[TH][@@]\1", TEXT)
            # TEXT = re.sub("([a-z]+[0-9๐-๙]*)\s*([ก-๐]+[0-9๐-๙]*)",
            #             r"\1\n[TH][@@]\2", TEXT)
            # TEXT = re.sub("([ก-๐]+[0-9๐-๙]*)\s*([a-z]+[0-9๐-๙]*)",
            #             r"\1\n[EN][@@]\2", TEXT)
            # # Split by Char
            # TEXT = [word.strip() for word in re.split("\n", TEXT)]
            return text, 500
        else:
            return "", 502

    '''                                                                                                                  
    Num to text                                                                                                         
    ---------------- Input ---------------                                                                               
    data = 1                                                                                                            
    --------------- Output ---------------                                                                               
    str(data), int(statuscode)                                                                                           
    '''
    def numth(self, data=""):
        new_data, number_search, state, n = "", "", 0, ""
        for ch in data:
            state = self.checknum(data=ch)
            if state:
                number_search += ch
            else:
                if number_search != "":
                    n = num_to_thaiword(int(number_search))
                new_data += n + ch
                n, number_search = "", ""
        return new_data, 600

    @staticmethod
    def checknum(data=""):
        try:
            unicodedata.numeric(data)
            return True
        except (TypeError, ValueError):
            return False

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
            tokenword = [word for word in tokenword if len(word) > 1 and word not in self.custom_words_stopwords]
            tokenword = [word for word in tokenword if word not in self.stopwords_eng and word not in self.stopwords_thai]
            for word in tokenword:
                if isthai(word):
                    tokenwords_thai.append(word.replace(' ', ''))
                else:
                    tokenwords_eng.append(word.replace(' ', ''))
            # print(tokenwords_thai)
            # print(tokenwords_eng)
            # return [tokenwords_thai, tokenwords_thai], 600
        except RuntimeError:
            return [], 601

        # POS Tag
        try:
            poswordsthai_noun = thai_tag(tokenwords_thai, engine='artagger', corpus='orchid')
            poswordsthai_noun = [item[0] for item in poswordsthai_noun if (item[1] == "NCMN" and item[0])]
            poswordseng_noun = eng_tag(tokenwords_eng)
            poswordseng_noun = [item[0] for item in poswordseng_noun if (item[1] not in ["IN"]and item[0])]
            poswords_noun = poswordseng_noun + poswordsthai_noun
        except RuntimeError:
            return [], 602
        return poswords_noun, 600
