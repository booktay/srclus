from srcmodel import srcmodel
srcm = srcmodel()

def main():
    try:
        srcm.poolCreateModel([100000, 400000, 100000])
        # srcm.runToken([100000, 100020])
    except KeyboardInterrupt:
        print("Ctrl C")

if __name__ == '__main__':
    main()
