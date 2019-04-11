#!/usr/bin/env python
# coding: utf-8
# author: Siwanont Sittinam
# description: temp module

# General Module
import os
import sys


# My Module
# sys.path.insert(0, os.path.abspath(''))
from srcluslib.utility.iorq import IORQ
from srcluslib.corpus.pantip import Pantip
from srcluslib.model.tokenize import Tokenize

iorq = IORQ()
pantip = Pantip()
data = pantip.requestthread(thread="37681939")  # "35421656", "33869381"
data = list(data[0].values())[0]
# iorq.print(data)
# print("-"*30)
tk = Tokenize()
rep, status_url = tk.replaceurl(data=data + "https://sta.com/q/9138112/looping-over" + "https://stw.com/qs/9138/?=loop")
rep, status_f = tk.filtertheng(data=rep)
iorq.print([rep, status_f])
rep, status_nt = tk.numth(data=rep)
rep, status_t = tk.run(data=rep)
# iorq.print([rep, status_t])

