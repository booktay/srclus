#!/usr/bin/env python
# coding: utf-8
# -------------------------
# Siwanont Sittinam
# lib/Word Corpus
# -------------------------

# Import NLP Module
from pythainlp.corpus import stopwords as pythai_stopword
from nltk.corpus import stopwords as nltk_stopword

class word:
    def __init__(self):
        # self.CUSTOM_STOP = CUSTOM_WORD
        pass

    def allWordTH(self):
        return self.customWordTH() + self.stopWordTH()

    def allWordENG(self):
        return self.customWordENG() + self.stopWordENG()
    
    def allWord(self):
        return self.allWordTH() + self.allWordENG()

    def customWordSpecial(self):
        return ["▃", "^", "๐๐๐๐๐๐"]

    def customWord(self):
        return self.customWordTH() + self.customWordENG()

    def customWordTH(self):
        return ["โง้บ", "โง้ย",  "พันติ๊บ", "ประมาท", "มาก", "มาการอง"]

    def customWordENG(self):
        return []

    def stopWordTH(self):
        return pythai_stopword.words('thai') + ["กล่าว","กว่า","กัน","กับ","การ","ก็","ก่อน","ขณะ","ขอ","ของ","ขึ้น","คง","ครั้ง","ความ","คือ","จะ","จัด","จาก","จึง",
        "ช่วง","ซึ่ง","ดัง","ด้วย","ด้าน","ตั้ง","ตั้งแต่","ตาม","ต่อ","ต่าง","ต่างๆ","ต้อง","ถึง","ถูก","ถ้า","ทั้ง","ทั้งนี้","ทาง","ทำ","ทำให้","ที่","ที่สุด","ทุก","นอกจาก","นัก",
        "นั้น","นำ","นี้","น่า","บาง","ผล","ผ่าน","พบ","พร้อม","มา","มาก","มี","ยัง","รวม","ระหว่าง","รับ","ราย","ร่วม","ลง","วัน","ว่า","สำหรับ","สุด","ส่ง","ส่วน","หนึ่ง",
        "หรือ","หลัง","หลังจาก","หลาย","หาก","อยาก","อยู่","อย่าง","ออก","อะไร","อาจ","อีก","เขา","เข้า","เคย","เฉพาะ","เช่น","เดียว","เดียวกัน","เนื่องจาก","เปิด","เปิดเผย",
        "เป็น","เป็นการ","เพราะ","เพื่อ","เมื่อ","เรา","เริ่ม","เลย","เห็น","เอง","แต่","แบบ","แรก","และ","แล้ว","แห่ง","โดย","ใน","ให้","ได้","ไป","ไม่","ไว้", "เเต่", "เเล้ว", 
        "ค่ะ", "ครับ", "ไง", "โอเค", "มั้ย", "แหะ", "จร้า", "หรอ", "มอย", "อยู่", "โอ้ย", "อย่า", "จำนวน"]
    
    def stopWordENG(self):
        return nltk_stopword.words('english') + ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also",
        "although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", 
        "are", "around", "as",  "at", "back","be","became", "because","become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", 
        "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", 
        "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough",
        "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", 
        "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", 
        "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", 
        "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", 
        "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", 
        "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", 
        "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps", "please", "put", "rather", 
        "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", 
        "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", 
        "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", 
        "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", 
        "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", 
        "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", 
        "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"] + ["url"]