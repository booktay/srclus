#!/usr/bin/env python
# coding: utf-8
# -------------------------
# Siwanont Sittinam
# Modeling for CLustering
# -------------------------

# Import Generate Command Module
import argparse
# Import Basic Module
import sys
import os
import requests
import time
# Import Text Module
import json
import re
# Import Math Module
import math
import random
from six.moves import xrange
# Import Tuple Module
import collections
import zipfile
import itertools
# Import Main Module
import tensorflow as tf
import pythainlp
import numpy as np
import deepcut as dc
from sklearn.manifold import TSNE
# Import Multiprocessing Module
from multiprocessing import Pool

# Search Result Clustering on Thai Internet Forum
parser = argparse.ArgumentParser()
parser.add_argument("a")
args = parser.parse_args()
print(args.a)
