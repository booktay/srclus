from srcmodel import srcmodel
srcm = srcmodel()

def main():
    try:
        srcm.poolCreateModel([100000, 101000, 400])
        # srcm.runToken([100000, 100020])
    except KeyboardInterrupt:
        print("Ctrl C")

if __name__ == '__main__':
    main()
