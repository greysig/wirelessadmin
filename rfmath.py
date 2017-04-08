#!/usr/bin/env python
#
''' Studying for the CWNA and wrote this to do the math for me to check and understand the examples better.

you can solve for dBm or mW using the math.log function for a more accurate that number or use the rules of 3s and 10s to get close '''

 
import math

def solve_dBm():
	mW=input('What is your mW? ')
	dBm = 10*(math.log10(mW))
	print ' '
	print 'Your dBm is: ', dBm


def solve_mW():
	dBm=input('What is your dBm? ')
	mW=math.pow(10,(dBm/10))
	print ''
	print 'Your mW is: ',mW
	



def ruleofrules():
	total_dBm=0
	total_mW=1
	print 'Super lazy code using the rule of 10s and 3s to find dBm or mW :)'
	print ' '
	num=''	
	while(num != 0):
				
		print 'Add or Subtract 10 or 3 for you target goal'
		print 'Quit [0]'
		print 'Restart [8]'
		print ''
		num = input (' ')
				  
		if (num == 3):
			total_dBm= total_dBm+3 
			total_mW= total_mW*2
			print 'Current', total_dBm, 'dBm :: ',total_mW, 'mW'
					
		elif (num == -3):
			total_dBm= total_dBm-3
			total_mW= total_mW/2
			print 'Current', total_dBm, 'dBm :: ',total_mW, 'mW'

		elif (num == 10):
			total_dBm= total_dBm+10
			total_mW= total_mW*10
			print 'Current', total_dBm, 'dBm :: ',total_mW, 'mW'
				
		elif (num == -10): 
			total_dBm= total_dBm-10
			total_mW= total_mW/10
			print 'Current', total_dBm, 'dBm :: ',total_mW, 'mW'
			print ''	
				
		elif (num==8):
			total_dBm=0
			total_mW=1
			print 'Current', total_dBm, 'dBm :: ',total_mW, 'mW'
			print '' 

		else:
			print 'Current', total_dBm, 'dBm :: ',total_mW, 'mW'

			print 'Choose a number that is 10, 3, -10, -3 :P '
				

	
	
def menu():
	print 'Calculating dBm or mW with log or use Rule of 10s or 3s'
	print ''
	opt= ''
	while (opt != 0):
		print 'Calculate dBm choose [1]'
        	print 'Calculate mW  choose [2]'
		print 'Rules of 3s and 10s  [3]'
        	print 'Quit [0]'
		print ''
		print ''
		opt  = input('What would you like to do?\n')
		
		if ( opt == 1):
			solve_dBm()
				
		
		elif (opt ==2):
			solve_mW()
			

		elif (opt == 3):
			ruleofrules()
							

menu()
