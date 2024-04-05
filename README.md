# Wakey

Completely disables the ability for a mac to sleep. 

I use this to keep my mac available when in clamshell mode. I use Synergy to connect my peripherals, which means my mouse can not wake the machine.

# Usage

The program must use sudo in order to run change the mac system settings. 

Option 1: 

This will disable sleep and hang. Once you terminate the program, sleeping will be re-enabled.
```bash
sudo python {repo_dir}/wakey.py
```

Option 2: 

If you would like to avoid leaving the wakey program hanging / occupying a terminal window, you can also use the -on and -off flags.

To disable sleep
```bash
sudo python {repo_dir}/wakey.py -on
```

To enable sleep
```bash
sudo python {repo_dir}/wakey.py -off
```
