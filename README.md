# Silly CMU-Q Printer Adder

This simple script (forked and personalized from https://github.com/Rewzilla/pc-mobility-print)
just adds CMU-Q's Secure Printer Queue to a Linux machine.

It logs into the print server and gets a unique print queue URL that doesn't require
username/password authentication everytime you want to print.  This makes things much
more compatible due to so many Linux implementations of keyrings being broken with
printers.

## FAQ

- Is it really safe to type in my CMU-Q username and password?  
  You should always be wary.  This code is pretty simple, though, so feel free to audit it.