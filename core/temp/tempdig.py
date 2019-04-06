def collectPantip(io=None):
        datas = [{},{}]
        rangethread = [8000001, 8580770]
        for i in range(rangethread[0], rangethread[1] + 1):
            thread = str(3*10**7 + i)
            try:
                data, status = io.requestPantipthread(thread=thread, security=True)
                if status == 400 : 
                    datas[0] = {**datas[0], **data}
                else:
                    datas[0][thread] = ""
                    datas[1][thread] = status
                if i % 10000 == 0 or i == int(rangethread[1]):
                    io.writeJson(filename=thread+".json", filepath="datas/raw/39/", data=datas)
                    datas = [{},{}]
            except KeyboardInterrupt:
                print("[Cancel] Ctrl-c Detection")
                break
                sys.exit(0)

    def checkCollectPantip(io=None):
        folderpath="../../datas"
        folders = os.listdir(folderpath)
        tempforrequest = []
        count = 0
        for folder in folders:
            filepaths = os.path.join(folderpath, folder)
            for filename in os.listdir(filepaths):
                data, status = io.readJson(filename=filename, filepath=filepaths)
                count+=1
                for name, status in data[1].items():
                    # io.print([name, status])
                    if status == 401:
                        tempforrequest.append(name)
        io.print([count, tempforrequest])