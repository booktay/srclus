import sys, os, requests, json, time, re
from multiprocessing import Pool
from six.moves import xrange
# Import NLP Module
import deepcut
from nltk.tokenize import word_tokenize
from pythainlp.tag import pos_tag
import nltk
from .word import word
# Import Hide Header
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class srclusdata:
    def replaceText(self, TEXT=""):
        # General
        TEXT = TEXT.lower()
        # Remove Another Language
        TEXT = re.sub(r'[^!-~ก-๙\s]+', r'', TEXT)
        # Link URL
        TEXT = re.sub(r'(http[s]?://)?([a-zก-ฮ0-9]+[.]?[a-zก-ฮ0-9]+)[.][a-zก-ฮ]+[/&?.=\-\w]*', r'URLLINK', TEXT)
        # Duplicate Char
        TEXT = re.sub(r'555+|ถถถ+', 'ตลก', TEXT)
        TEXT = re.sub(r'([a-zก-๙])\1{3,}', r'\1', TEXT)
        TEXT = re.sub(r'([a-zก-๙])\1{2,}\s+', r'\1 ', TEXT)
        # Time
        TEXT = re.sub(r"(\d+)\s(ชั่วโมง|นาที|วินาที)", r"\1\2", TEXT)
        TEXT = re.sub(r"(\d+)\s(hour|minute|second|sec[s]?)", r"\1\2", TEXT)
        # Word Space
        TEXT = re.sub(r"(\d+)([.)])\s([a-zก-๙]+)", r"\1\2\3", TEXT)
        TEXT = re.sub(r"([a-zก-๙]+)\s(\d+)\s(%)", r"\1\2\3", TEXT)
        TEXT = re.sub(r"([a-zก-๙]+)[\s\-](\d+)\s", r"\1\2 ", TEXT)
        TEXT = re.sub(r"\s+(and|or)\s+", r"\1", TEXT)
        TEXT = re.sub(r"\s+[0-9]+\s+", " ", TEXT)
        # Special Char
        TEXT = re.sub(r"[<(\{\[\\/#]+\s*(\w+)\s*[>)\}\]\\/#]+", r"\1 ", TEXT)
        TEXT = re.sub(r'[@!-/:->\[-`{-~]+', '', TEXT)
        TEXT = re.sub(r'[:/&?#.\-ๆ]', '', TEXT)
        TEXT = re.sub(r'(\s)\1{1,}',r'\1', TEXT)
        # Add Multilanguage Detect
        TEXT = re.sub("(^[a-z]+[0-9๐-๙]*)", r"[EN][@@]\1", TEXT)
        TEXT = re.sub("(^[ก-๐]+[0-9๐-๙]*)", r"[TH][@@]\1", TEXT)
        TEXT = re.sub("([a-z]+[0-9๐-๙]*)\s*([ก-๐]+[0-9๐-๙]*)", r"\1\n[TH][@@]\2", TEXT)
        TEXT = re.sub("([ก-๐]+[0-9๐-๙]*)\s*([a-z]+[0-9๐-๙]*)", r"\1\n[EN][@@]\2", TEXT)
        # Split by Char
        TEXT = [word.strip() for word in re.split("\n", TEXT)]
        return TEXT

# 2