#!/usr/bin/env python
# coding: utf-8
# -------------------------
# Siwanont Sittinam
# lib/Preprocess Data
# -------------------------

# Import General Module
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

    def __init__(self):
        self.TIME = time.strftime("%Y%m%d%H%M")
        self.WORD = word()
    
    def loadFile(self, PATH="", NAME=""):
        print("[Load] " + NAME + " file")
        PATHFILE = os.path.join(PATH, NAME + ".json")
        with open(PATHFILE, mode='r', encoding='utf-8') as data:
            WORDS = json.load(data)
            print("[Success] " + NAME + " file")
            return WORDS

    def createFile(self, DATA=[], PATH="", NAME=""):
        print("[Create] " + NAME + "." + self.TIME + " file")
        if not os.path.exists(PATH):
            os.mkdir(PATH)
        PATHFILE = os.path.join(PATH, NAME + ".json")
        access = 'x' if not os.path.exists(PATHFILE) else 'w'
        with open(PATHFILE, mode=access, encoding='utf-8') as data:
            json.dump(DATA, data, ensure_ascii=False, indent=2)
            print("[Success] " + NAME + "." + self.TIME + " file")

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
    
    def replaceWord(self, WORDS=[]):
        WORDS = [word for word in WORDS if re.match(r'[a-zก-๐]+', word) is not None]
        return WORDS

    def tokenizeText(self, TEXT=""):
        try:
            # Replace Text By Regex
            TOKEN_WORD = self.replaceText(TEXT)
            # Tokenize Text
            TOK_ENG = ' '.join([TOK.split("[@@]")[1] for TOK in TOKEN_WORD if TOK.split("[@@]")[0] == "[EN]"])
            TOK_TH = ' '.join([TOK.split("[@@]")[1] for TOK in TOKEN_WORD if TOK.split("[@@]")[0] == "[TH]"])
            # print(TOK_ENG, TOK_TH)
            TOKEN_TH = [word for word in deepcut.tokenize(TOK_TH, custom_dict=self.WORD.customWord()) if word not in [' ','']]
            TOKEN_ENG = [word for word in re.split(' ', TOK_ENG) if word not in [' ','']]
            # Part of Speech Tagger
            TOKEN_TH = pos_tag(TOKEN_TH, engine='artagger')
            TOKEN_TH = [item[0] for item in TOKEN_TH if item[1] == "NCMN" and item[0] not in self.WORD.stopWordTH()]
            TOKEN_ENG = nltk.pos_tag(TOKEN_ENG)
            TOKEN_ENG = [item[0] for item in TOKEN_ENG if item[1] == "NN" and item[0] not in self.WORD.stopWordENG()]
            TOKEN_WORD = TOKEN_ENG + TOKEN_TH
            # Replace List of Word By Regex
            TOKEN_WORD = self.replaceWord(TOKEN_WORD)
            TOKEN_WORD = ' '.join(TOKEN_WORD)
            # print(POS_WORD)
        except:
            print('[Error] Tokenize Word')
            # print(*TEXT, sep=", ")
            return "", TEXT
        return TOKEN_WORD, ""

    def getWordFromUrl(self, THREAD_ID=30000000):
        # Define Variable
        BASE_PATH = "https://ptdev03.mikelab.net/kratoo/"
        URL = BASE_PATH + str(THREAD_ID)

        # Request
        try:
            RAW_REQUEST = requests.get(URL).json()
        except :
            print('[Error] URL Exceed : ' + str(THREAD_ID))
            return [], ""
        
        if (RAW_REQUEST["found"]):
            RAW_SOURCE = RAW_REQUEST["_source"]
            THREAD_WORD = RAW_SOURCE["title"] + " " + RAW_SOURCE["desc"]
            TOKEN_WORD, ERROR_WORD = self.tokenizeText(THREAD_WORD)
            return TOKEN_WORD, ERROR_WORD
        return [], ""

    def runGetFromUrl(self, THREAD=[1,2]):
        try:
            ALL_THREAD, ERROR_THREAD = [], []
            ALL_COUNT, ERROR_COUNT = 0, 0
            for THREAD_RUN in xrange(THREAD[0], THREAD[1] + 1):
                THREAD_ID = 30000000 + THREAD_RUN
                WORD_TOKEN, ERROR_TOKEN = self.getWordFromUrl(THREAD_ID)
                if WORD_TOKEN and ERROR_TOKEN is "" : 
                    ALL_THREAD.append({THREAD_RUN:WORD_TOKEN})
                    ALL_COUNT += 1
                elif not WORD_TOKEN: 
                    ERROR_THREAD.append({THREAD_RUN:ERROR_TOKEN})
                    ERROR_COUNT += 1
                # File_Size_Modified
                FILE_SIZE = 5
                if (THREAD_RUN != THREAD[0] and THREAD_RUN % FILE_SIZE == 0) or (THREAD_RUN == THREAD[1]):
                    if len(ALL_THREAD) > 0:
                        TOKEN_NAME = "token" + "." + self.TIME + "." + str(THREAD_RUN-FILE_SIZE+1) + "." + str(THREAD_RUN)
                        self.createFile(DATA=ALL_THREAD, PATH="result/token/" , NAME=TOKEN_NAME)
                    if len(ERROR_THREAD) > 0:
                        ERROR_NAME = "error" + "." + self.TIME + "." + str(THREAD_RUN-FILE_SIZE+1) + "." + str(THREAD_RUN)
                        self.createFile(DATA=ERROR_THREAD, PATH="result/error/", NAME=ERROR_NAME)
                    print("[Save] file at thread " + str(THREAD_ID) + " " + str(ALL_COUNT) + "/" + str(ERROR_COUNT))
                    ALL_THREAD, ERROR_THREAD = [], []
                if THREAD_RUN == THREAD[0]:
                    print("[Start] Thread " + str(THREAD_RUN) + " getFromurl " + str(ALL_COUNT) + "/" + str(ERROR_COUNT))
                if THREAD_RUN == THREAD[1]:
                    print("[Success] Finish getFromurl " + str(ALL_COUNT) + "/" + str(ERROR_COUNT))
        except KeyboardInterrupt:
            print("\n[Cancel] Ctrl-c Detection at runGetFromUrl()")
            sys.exit(0)
    
    def createPoolGetFromUrl(self, PROCESS=1):
        try :
            print("[Initial] Create "+ str(PROCESS) + " processes")
            # Input Thread range
            ALL_THREAD = []
            for i in range(1, PROCESS+1):
                THREAD_MIN = int(input("[Process " + str(i) +"] Start Thread : "))
                THREAD_MAX = int(input("[Process " + str(i) +"] Stop Thread : "))
                ALL_THREAD.append([THREAD_MIN, THREAD_MAX])
            with Pool(processes=PROCESS) as pool:
                pool.map(self.runGetFromUrl, ALL_THREAD)
            print("[Success] "+ str(PROCESS) + " processes")
        except KeyboardInterrupt:
            print("\n[Cancel] Ctrl-c Detection at createPool()")
            sys.exit(0)