from srcmodel import srcmodel
srcm = srcmodel()

def main():
    # srcm.poolCreateModel(START=1*10**5, STOP=2*10**5, ITERATION=2*10**4)
    srcm.poolCreateModel(START=1*10**5, STOP=1*10**5 + 500, ITERATION=100)
    # srcm.poolCreateModel(START=1*10**5, STOP=1*10**5 + 10, ITERATION=2)

if __name__ == '__main__':
    main()
