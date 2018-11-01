from srcmodel import srcmodel
from multiprocessing import Pool
from six.moves import xrange

srcm = srcmodel()

def runToken(THREAD=[0,1]):
    TOKEN_THREAD = []
    for THREAD_RUN in xrange(THREAD[0], THREAD[1]):
        WORD_TOKEN = srcm.getTokenWordFromUrl(THREAD_RUN)
        TOKEN_THREAD += WORD_TOKEN
        if THREAD_RUN % 10 == 0:
            print("At Thread : " + str(THREAD_RUN))
    srcm.createFile(DATA=TOKEN_THREAD, NAME="token." + str(THREAD[0]) + "." + str(THREAD[1]))
    # return []

def main():
    ALL_THREAD = [[x, x + 2 * 10**4] for x in range(1 * 10**5, 3 * 10**5, 2 * 10**4)]
    with Pool(processes=len(ALL_THREAD)) as pool:
        pool.map(runToken, ALL_THREAD)
    # return TOKEN_THREAD
    
    


if __name__ == '__main__':
    main()
