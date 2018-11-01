from srcmodel import srcmodel
srcm = srcmodel()

def main():
    # srcm.poolCreateModel(START=1*10**5, STOP=2*10**5, ITERATION=2*10**4)
    srcm.poolCreateModel(START=1*10**5, STOP=1*10**5 + 1000, ITERATION=200)
    # srcm.poolCreateModel(START=1*10**5, STOP=1*10**5 + 10, ITERATION=2)

if __name__ == '__main__':
    main()
