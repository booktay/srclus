import os
import json
import time
# from six.moves import urllib
from six.moves import xrange
from sklearn.manifold import TSNE
import numpy as np
import matplotlib
from matplotlib import rcParams
matplotlib.rc('font', family='Garuda')
import matplotlib.pyplot as plt
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Garuda']

def loadFile(NAME):
    with open(os.path.join('data/' + NAME + '.json'), mode='r', encoding='utf-8') as store_word:
        WORD_TOKEN_ALLTHREAD = json.load(store_word)
    return WORD_TOKEN_ALLTHREAD

def plot(low_dim_embs, labels, filename='tsne_thai_'+ time.strftime("%Y%m%d%H%M") +'.png'):
    assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
    plt.figure(figsize=(30, 30))
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(label, xy=(x, y), xytext=(5, 2), textcoords='offset points', ha='right', va='bottom', fontname='Garuda')
    plt.savefig(filename)
    print("[Success] Plot Graph : " + filename)

def main():
    try:
        print("[Init] Import dataset")
        plot_name = input('Input plot filename : ')
        plot_data = loadFile(plot_name)
        print("[Init] Build Graph ....")
        plot(plot_data['low_dim_embs'], plot_data['labels'])
        print("[Success] Plot")
    except KeyboardInterrupt:
        print("[Cancel] Ctrl-c Detect")
    except Exception:
        print("[Error] Exception Found")
    finally:
        print("[Close] ")


if __name__ == '__main__':
    main()
