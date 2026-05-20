#!/usr/bin/env python3

HOST="print.qatar.cmu.edu"
PRINTER="CampusPrinting"
DRIVER="hp-color_laserjet_mfp_e87760-ps.ppd.gz"

import getpass
from pcmobilityprint import *

def main(server, username, password, verify_ssl = False):

	pcmp = PCMobilityPrint(server=server)
	
	if verify_ssl:
		pcmp.verify_ssl = True
	else:
		pcmp.verify_ssl = False

	if not pcmp.authenticate(username, password):
		print("Authentication error")
		return

	pcmp.add_printer(PRINTER, driver=DRIVER)

if __name__ == "__main__":
	# Get the username from the user
	username = input("Username: ")

	# Get the password (safely, printing star)
	password = getpass.getpass("Password: ")


	main(server=HOST, username=username, password=password)
