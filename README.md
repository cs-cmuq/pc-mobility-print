# Silly CMU-Q Printer Adder

This simple script (forked and personalized from https://github.com/Rewzilla/pc-mobility-print)
just adds CMU-Q's Secure Printer Queue to a Linux machine.

It logs into the print server and gets a unique print queue URL that doesn't require
username/password authentication everytime you want to print.  This makes things much
more compatible due to so many Linux implementations of keyrings being broken with
printers.

## Usage

1. If you have the campus printer installed and it isn't working, delete it and reboot.  (Yes, you do need to reboot.  No, I don't know why.)
2. Run this script: `python3 ./cmuq.py`
3. Enter your username
4. Enter your password
5. Says "y"
6. Done.

## FAQ

- Is it really safe to type in my CMU-Q username and password?  
  You should always be wary.  This code is pretty simple, though, so feel free to audit it.