import sys
import os
import requests
import json
import multiprocessing as mp

def opt_file(data, data_path, opt):
    try:
        with open(data_path, mode=opt, encoding='utf-8') as store_word:
            store_word.write(data)
    except FileExistsError:
        print("[Error] Found File in directory")
        return

def running(i, N, data_path):
    base_path = "https://ptdev03.mikelab.net/kratoo/"

    data = ""

    opt_file(data,data_path,'x')

    run_number = i

    try:
        print("Start at thread_id : " + str(30000000 + run_number))
        while run_number <= N:
            thread_id = 30000000 + run_number
            url = base_path + str(thread_id)
            r = requests.get(url).json()
            if (r['found']):
                source_inthread = r['_source']
                data = data + source_inthread['title'] + source_inthread['desc'] #source_inthread['comments_desc']
            run_number += 1
            if (run_number / (N + i) * 100) % 5 == 0: print('Process % : ' + str(run_number / N * 100) + ' at thread_id : ' + str(30000000 + run_number))
        print("End at thread_id : " + str(30000000 + run_number) + "at path : " + data_path)
    except KeyboardInterrupt:
        print("Stop at thread_id : " + str(30000000 + run_number))
    except Exception:
        print("[Error] Exception Found ")
    finally:
        opt_file(data, data_path, 'a')

def main():

    processes = []
    for num in range(0,9):
        i = [(num * 10**6), ((num * 10**6) + 999999)]
        p = mp.Process(target=running, args=( i[0], i[1] , "data/store_word." + str(num) + ".txt"))
        p.start()
        processes.append(p)

    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print("Cancel by user")
    except Exception:
        print("[Error] Exception Found ")
    finally:
        print("Closed")

if __name__ == '__main__':
    main()