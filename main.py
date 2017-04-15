#! /usr/bin/env python


import rfmath

import wireless_network


def main():
	print'Hi learning out to using multifiles'
	print'option 1 rfmath is basic math I read studying for the CWNA'
	print'option 2 If you have a kismet.netxml file, it should give you basic input fromt the, not thing fancy'
	opt=input('What would you like to do?  ')
	if opt==1:
		rfmath.main_menu()
	if opt==2:
		wireless_network.kismet_main()





main()
