from srcmodel import srcmodel
srcm = srcmodel()

def main():
    srcm.poolCreateModel(START=10**5, STOP=2*10**5, ITERATION=2*10**4)

if __name__ == '__main__':
    main()
