from srcmodel import srcmodel
srcm = srcmodel()

def main():
    try:
        srcm.poolCreateModel([100000, 200000, 20000])
        # srcm.runToken([100000, 100040])
    except KeyboardInterrupt:
        print("Ctrl C")
        return 

if __name__ == '__main__':
    main()
