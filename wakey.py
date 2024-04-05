'''
Completely disables the ability for this mac to sleep while running. Upon 
cancelling the command in terminal, sleeping becomes possible again. Can also
use the -on and -off flags to avoid leaving the command hanging.

** Must be ran with sudo to work properly. **
'''
import argparse
import subprocess
import signal

def set_sleep(disable):
    cmd = 'pmset disablesleep {}'.format(int(disable))
    subprocess.run(cmd, shell=True)
    state = "disabled" if disable else "enabled"
    print(f"Sleep has been {state}.")

def exit_handler(signum, frame):
    print("\nRestoring sleep settings...")
    set_sleep(False)
    exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Control Mac Sleep Mode')
    parser.add_argument('-on', action='store_true', help='Disable sleep mode')
    parser.add_argument('-off', action='store_true', help='Enable sleep mode')

    args, unknown = parser.parse_known_args()
    
    # Default behavior when no flags are provided
    if not any(vars(args).values()):
        signal.signal(signal.SIGINT, exit_handler)
        set_sleep(True)
        print("Your mac is holding its eyes open. Press Ctrl+C to allow it to sleep.")
        signal.pause()
    else:
        if args.on:
            set_sleep(True)
        elif args.off:
            set_sleep(False)
