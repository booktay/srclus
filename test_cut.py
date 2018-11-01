from srcmodel import srcmodel
srcm = srcmodel()

def main():
    srcm.poolCreateModel([100000, 101000, 300])
    # srcm.runToken([100000, 101000])

if __name__ == '__main__':
    main()
