#!/usr/bin/env python
# coding: utf-8
import os
import json
from word2vec import word2vec
from srcmodel import srcmodel

src = srcmodel()

word = ["ตรวจการ บ้าน Hokkaido หน่อย ค่าา ค่ะ ตุลา","Hakodate เครื่อง บิน Hakodate เที่ยง Hakodate ตุลา","Hakodate ตุลา  Sapporo JR Hakodate  Sapporo Sapporo ตุลา  Otaru Sapporo ตุลา  ตุลา  Sapporo Sapporo ตุลา CTSBKK แผน หน่อย ค่ะ ไหว มั้ย ค่ะ นิดนึง ค่ะ วัน ตุลา วัน วัน Furano Tomita farm มั้ย คะ ฤดู มั้ย มั้ย คะ Furano เมือง คะ Asahikawa Noburibetsu jigokudani ค่ะ Toya Biei ส่วน","ค่ะ คุ้มมั้ย เมืองไกล Sapporo วัน รวด จำนวน วัน โอเค มั้ย คะ ตอน ตั๋ว เครื่อง บิน เมือง วัน ค่ะ นะ คะ"]
print(src.clean(word))
