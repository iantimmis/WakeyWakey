'''
Completely disables the ability for this mac to sleep while running. Upon 
cancelling the command in terminal, sleeping becomes possible again. 

** Must be ran with sudo to work properly. **
'''

import atexit
import subprocess

def exit_handler():
    subprocess.run('pmset disablesleep 0', shell=True)

if __name__ == "__main__":
    atexit.register(exit_handler)

    subprocess.run('pmset disablesleep 1', shell=True)

    # with open("wakey_logo.txt") as f:
        # print(f.read())

    print("Your mac is holding its eyes open...")

    while True:
        pass
