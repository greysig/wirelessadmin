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
	mW=math.pow(10,(dBm/float(10)))
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
		num = input ('')
			  
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
			total_mW= total_mW/float(10)
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
			
def fresnel_midpoint():
#calculate the radius of the first Fresnel zone at the mid point between two antennas
	print '================================================='
	print 'Calulating the Fresnel Zone either whole zone or the minimum of 60% at midpoint of two antennas'
	print''
	D=input(' What is the distance of the link in miles?  ')
	print float(D)
	print '' 
	F=input('What is the transmitting freqency in GHz')
	print float(F)
	print''
	print ' [1] Calculate the whole zone '
	print ' [2] Calculate the minimun 60% unobstructed zone'
	print' [0] Quit '
	opt=input('::')
	if opt == 1:
		radius=(72.2*(math.sqrt(D/float(4)*F)))
		print  'Radius is: ',radius
		print 	'Optimal clearence that you will want along the singal path.'
		print''
		
	if opt == 2:
		#calculate the min 60% unobstructed
		radius = 43.4*(math.sqrt(D/float(4)*F))
		print 'Min radius: ',radius


	
		

def fresnel_anypoint():

	#calculate the fresnel zone at any point between two antennas

	print'Calculating the fresnel zone at any point between two antennas'
	print''
	N = input('Which Fresenel Zone are you calculating?  ')
	print ' First what is distance from the obstacle \(in miles\) to the first antenna?  '
	d1=input('D1: ')
	print '  Now the distance between the obstacle \(in miles\) to the other antenna?  '
	d2=input('D2: ')
	float(d1)
	float(d2)
	D= (d1+d2)
	float(D)
	print''
	print ' What is the Frequency in  GHZ? '
	print''
	F=input('GHz: ')
	float(F)
	radius= 72.2*math.sqrt((N*d1*d2)/(F*D))
	print ''
	print ' Your radius is:  ',radius



def fres_menu():
	loop=1
	while loop==1:
		print'====================================='
		print"Calculate the Fresnel zone"
		print''
		print' [1] Calculate at midpoint between two antennas '
		print' [2] Calculate at any point between two antennas ' 
		print' [0] Back '
		opt=input('::')
	
		if opt==1:
			print''
			fresnel_midpoint()

		if opt==2:
			print''
			fresnel_anypoint()
		
		if opt==0:
			break

def math_menu():
		print 'Calculating dBm or mW with log or use Rule of 10s or 3s'
		print ''
		opt= ''
		while (opt != 0):
			print 'Calculate dBm choose [1]'
       		 	print 'Calculate mW  choose [2]'
			print 'Rules of 3s and 10s  [3]'
        		print 'Fresnel Zone 	    [4]'	
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
								
	
			elif (opt==4):
				fres_menu()
			

			elif opt==0:

				break




math_menu()
