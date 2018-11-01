from srcmodel import srcmodel
srcm = srcmodel()

def main():
    srcm.poolCreateModel([100000, 101000, 200])
    # srcm.runToken([100,200])

if __name__ == '__main__':
    main()
