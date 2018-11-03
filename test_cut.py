from srcmodel import srcmodel
srcm = srcmodel()

def main():
    try:
        A, B, C = [int(x) for x in input("Enter Start Stop Step : ").split()]
        srcm.poolCreateModel([A, B, C])
        # srcm.runToken([100000, 100040])
    except KeyboardInterrupt:
        print("Ctrl C")
        return 

if __name__ == '__main__':
    main()
