import os

def merge_file():
    try:
        paths = sorted(os.listdir('data'))
        with open(os.path.join('data/', 'store_word.txt'), mode='x', encoding='utf-8') as store_word:
            for path in paths:
                with open(os.path.join('data/', path), mode='r', encoding='utf-8') as new_words:
                    for word in new_words:
                        store_word.write(word)
                os.remove(os.path.join('data/', path))
    except FileExistsError:
        print("[Error] Found File in directory")
        return

if __name__ == '__main__':
    merge_file()