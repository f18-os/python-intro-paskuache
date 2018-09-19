import os
import sys
import subprocess
def trycatch():
    try:
        inp = input('$ ').split(' ')
        for x in inp:
            if x == 'exit':
                sys.exit()
            if x == 'clear':
                os.system('clear')
                trycatch()
            if x == 'wc':
                subprocess.call(['./p3-exec.py'])
                trycatch()
            if x == 'cd':
                subprocess.call(['./p4-redirect.py'])
                trycatch()
            trycatch()
    except IndexError:
        trycatch()
if __name__ == '__main__':
    trycatch()
