#! /usr/bin/env python

from  xml.etree.ElementTree import parse 



def networkAttrib ():
	number = network.get('number')
	sigType = network.get('type') 
	seenFirst = network.get('first-time')
	seenLast = network.get('last-time')

	return number, typeSig, seenFirst, seenLast


def ssidSeen():			
		for ssid in network.iterfind('SSID'):
			seenFirst = ssid.get('first-time') 
			seenLast = ssid.get('last-time')
			print seenFirst, seenLast

def ssidDetails(key):
	for network in doc.iterfind('wireless-network'):
		if network.get('number')==key:
			for detail in network.iterfind('SSID/'):
				try:
					print detail.tag+ ': '+detail.text
				except (TypeError):
					print'No essid'
					pass

def bssid(key):		
	for network in doc.iterfind('wireless-network'):
		if  network.get('number')==key:
			for bssid in network.iterfind('BSSID'):
				print 'BSSID:', bssid.text


def freq_channel(key):
	for network in doc.iterfind('wireless-network'):
                if network.get('number')==key:
			for freq in network.iterfind('freqmhz'):
				print freq.text +' in mhz'
			for channel in network.iterfind('channel'):
				print 'CH: ' + channel.text


def carrier(key):
	for network in doc.iterfind('wireless-network'):
                if network.get('number')== key:
			for carry in network.iterfind('carrier'):
				print 'Carrier: '+ carry.text

def encode(key):
	for network in doc.iterfind('wireless-network'):
                if network.get('number')==key:
			for encode in network.iterfind('encoding'):
				print 'Encoding: '+ encode.text


def wirelessClient(key):
	for network in doc.iterfind('wireless-network'):
		if network.get('number')==key:
			for client in network.iterfind('wireless-client'):
				print 'Client:',client.get('number'),'details.'
				print 'MAC Address: '+client.findtext('client-mac')
				print 'Channel: '+ client.findtext('channel')
				print 'Frequency: '+client.findtext('freqmhz')
				print"========================="
		

 
def infraopt():
	print' ========================================================'
	print' [1] List found ESSID '
	print' [2] Know the ESSID? Look it up '
	print' [0] Back '
	opt=input('Whats it going to be?  ')
	if opt==1:
		listNet()
		lookupNet()
	if opt==2:
		lookupNet()

def lookupNet():
		
	value=''
	value=raw_input('What is the name of the network?\n:')
	
	for keys, val in eD.iteritems():
		if val == value:
			key=keys
			loop=1
	
			while (loop==1):
				print' [1] Show wireless clients '
				print' [2] SSID details '
				print' [3] BSSID '
				print' [4] Frequency, Channel, Carrier, Encoding '
				print' [5] Print all '
				print' [0] Back'
	
				opt=input('\n#:')
				if (opt==1):
					print'=========================='
					wirelessClient(key)
					print'========================='
				if (opt ==2):
					print '========================'
					print value
					print 'SSID Details'
					ssidDetails(key)
					print '========================'
				elif (opt ==3):
					print '========================'
					print
					bssid(key)
					print '========================'
				elif (opt ==4):
					print '========================'
					print 
					print 'Frequency, Channel, Carrier, Encoding'
					freq_channel(key)
					carrier(key)
					encode(key)
					print '========================'
				elif (opt ==5):
					print '========================'
					print
					print'SSID Details'
					ssidDetails(key)
					bssid(key)
					freq_channel(key)
					carrier(key)
					encode(key)
					print'========================='
				elif (opt ==0):
		 			break
	
	


def listNet():
	print'========================================================='
	print eD.values()		
	print'========================================================='


def cloakedNet():
	print '======================================================'
	print 'There are' , len(cD.keys()), 'cloaked networks' 
	print ''
	print cD.values()
	print' ======================================================='


	value=''
        value=raw_input('What is the BSSID of the network?\n:')

	
        for keys, val in cD.iteritems():
		if val == value:
			key=keys

			loop =1
			while (loop == 1):
				print' [1] Show Clients and details '	
				print' [2] SSID details '
        	                print' [3] Frequency, Channel, Carrier, Encoding '
        	                print' [4] Print all '
       	        	  	print' [0] Back'
                       		opt=input('\n#:')
                       		if (opt==1):
					print'========================'
					wirelessClient(key)
					print'========================'
				if (opt ==2):
                                	print '========================'
                               		print value
					print 'SSID Details'
                                	ssidDetails(key)
                                	print '========================'
                        	elif (opt ==3):
                               		print '========================'
                               		print value
					freq_channel(key)
					carrier(key)
					encode(key)
                                	print '========================'
                               	elif (opt ==4):
                                	print '========================'
                                	print value
					print'SSID Details'
                                	ssidDetails(key)
                               		bssid(key)
                                	freq_channel(key)
                                	carrier(key)
                                	encode(key)
                                	print'========================='
                        	elif (opt ==0):
                                	break
        		

	
	
def infra():
	print'========================================================================='	
	print 'There are', len(eD.keys()),'ESSIDs and',len(cD.keys()),'Cloaked ESSIDs'
	print'=========================================================================='
	loop=1
	while (loop == 1):
		
		print (' [1]  Search known network ')
		print (' [2]  Cloaked Networks ' )
		print (' [0]  Back ')
		opt=input('\n: ')

		if (opt == 1):
			infraopt()

		elif(opt == 2):
			cloakedNet()

		elif (opt == 0):
			break

		else:
			print 'Not an option...'

def menu():
	loop=1
	
	print' Playing with kismet .netxml files?'
	print' What would you like to do...within the power of this little code :)'
	print''
	while ( loop == 1):
		print'========================================================'
		print' What would you like to do?'
		print' [1] To access infrastructure networks '
		print' [2] To access probes '
		print' [0] To Exit '
		opt=input('\n :')
		if (opt == 1):
			infra()
		elif (opt == 2):
			probes()
		elif (opt == 0):
			break
		else:
			print 'Not an option'	


def essidE():
	for network in doc.iterfind('wireless-network'):
		if network.get('type') == 'infrastructure':
			for ssid in network.iterfind('SSID'):
				if ssid.findtext('essid') != '':
					eD[network.get('number')]=ssid.findtext('essid')
					print 'ESSID Network Added'
				elif ssid.findtext('essid') =='':
					cD[network.get('number')]=network.findtext('BSSID')
					print 'Cloaked Network Added'
		elif network.get('type') == 'probe':
			pD[network.get('number')]='Probe Network'
			print 'Probe Network Added'



eD={}
cD={}
pD={}
print'================================================================='
print'================================================================='
xml=raw_input('Type the path and name of your file you wish to analys:  ')
u = open(xml, 'r') 
doc = parse(u)


print '======================================================='
essidE()
print '======================================================='
menu()									










