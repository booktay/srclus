# Import Basic Module
import sys
import os
import json
import requests
import time
import re
from pythainlp.tokenize import word_tokenize
from pythainlp.tag import pos_tag
from pythainlp.corpus import stopwords
from multiprocessing import Pool
from six.moves import xrange
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class srcmodel:

    def __init__(self):
        self.TIMENOW = time.strftime("%Y%m%d%H%M")
        self.CUSTOM_STOP = self.loadCustomStopword()

    def loadFile(self, NAME=""):
        WORDS = []
        PATH = os.path.join('data/', NAME + '.json')
        with open(PATH, mode='r', encoding='utf-8') as store_word:
            WORDS = json.load(store_word)
        return WORDS

    def createFile(self, DATA=[], NAME=""):
        if not os.path.exists('data'):
            os.mkdir('data')
        with open(os.path.join('data/', NAME + "." + self.TIMENOW + '.json'), mode='x', encoding='utf-8') as store_word:
            json.dump(DATA, store_word, ensure_ascii=False)

    def loadCustomStopword(self):
        with open('custom_word.json', mode='r', encoding='utf-8') as custom_word:
            CUSTOM_WORD = json.load(custom_word)
        return CUSTOM_WORD

    def replaceWord(self, TEXT=""):
        TEXT = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+','', TEXT)
        TEXT = re.sub(r'[@:.\&;=$#?+{}/\\()[\],><|!\*_"\'–·]', ' ', TEXT)
        TEXT = re.sub(r'[ๆ“”]', '', TEXT)
        # TEXT = re.sub(r'\s+(\d)+\s', r'\1', TEXT)
        TEXT = TEXT.strip()
        TEXT = re.split(' ', TEXT)
        return TEXT

    def tokenWord(self, TEXT=[]):
        POS_WORD = []
        try:
            for text in TEXT:
                POS_WORD += word_tokenize(text, engine='deepcut')
            #
            STOP = stopwords.words('thai')
            POS_WORD = [item for item in POS_WORD if item not in STOP]
            # print(*POS_WORD, sep=", ")
            POS_WORD = [item for item in POS_WORD if item not in self.CUSTOM_STOP]
            POS_WORD = pos_tag(POS_WORD, engine='artagger', corpus='orchid')
            POS_WORD = [item[0] for item in POS_WORD if item[1] == "NCMN"]
            # print(POS_WORD)
        except:
            print('[Error] Tokenization : ')
            # print(*TEXT, sep=", ")
            return [], POS_WORD
        return POS_WORD, []

    def getTokenWordFromUrl(self, THREAD_RUN=0):
        # Define Variable
        BASE_PATH = "https://ptdev03.mikelab.net/kratoo/"
        THREAD_ID = 30000000 + THREAD_RUN
        URL = BASE_PATH + str(THREAD_ID)

        # print(URL)
        # Request
        try:
            RAW_REQUEST = requests.get(URL).json()
        except :
            print('[Error] URL Exceed : ' + str(THREAD_ID))
            return [],[]
        
        if (RAW_REQUEST["found"]):
            RAW_SOURCE = RAW_REQUEST["_source"]
            TOKEN_TITLE = self.replaceWord(RAW_SOURCE["title"])
            TOKEN_DESC = self.replaceWord(RAW_SOURCE["desc"])
            # TOKEN_WORD = [TOKEN_TITLE + TOKEN_DESC]
            TOKEN_WORD, ERROR_TOKEN = self.tokenWord(TOKEN_TITLE + TOKEN_DESC)
            return TOKEN_WORD, ERROR_TOKEN
        return [], []
    
    def runToken(self, THREAD=[0,1]):
        TOKEN_THREAD = []
        ERROR_THREAD = []
        try:
            for THREAD_RUN in xrange(THREAD[0], THREAD[1]):
                WORD_TOKEN, ERROR_TOKEN = self.getTokenWordFromUrl(THREAD_RUN)
                if len(WORD_TOKEN) > 0 : TOKEN_THREAD.append(WORD_TOKEN)
                if len(ERROR_TOKEN) > 0 : ERROR_THREAD.append(ERROR_TOKEN)
                if THREAD_RUN % 10 == 0:
                    print("At Thread : " + str(THREAD_RUN))
            self.createFile(DATA=TOKEN_THREAD, NAME="token." + str(THREAD[0]) + "." + str(THREAD[1]))
            self.createFile(DATA=ERROR_THREAD, NAME="error.token." + str(THREAD[0]) + "." + str(THREAD[1]))
        except KeyboardInterrupt:
            print("Ctrl c")
            return []

    def poolCreateModel(self, RANGE = [0,0,0]):
        # 2 * 10**4
        ALL_THREAD = [[x, x + RANGE[2]] for x in range(RANGE[0], RANGE[1], RANGE[2])]
        PROCESS = len(ALL_THREAD)
        print("[Init] Generate " + str(PROCESS) + " processes")
        try :
            with Pool(processes=PROCESS) as pool:
                pool.map(self.runToken, ALL_THREAD)
        except KeyboardInterrupt:
            print("Ctrl c")
            return []
