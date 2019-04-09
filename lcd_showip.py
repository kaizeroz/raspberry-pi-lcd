from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni

listInterfaces = ni.interfaces()
listIP = []
for l in listInterfaces:
	try:
		'''
		ip_eth0 = ni.ifaddresses('eth0')[AF_INET][0]['addr']
		print(ip_eth0)
		'''
		ip = ni.ifaddresses(l)[AF_INET][0]['addr']
		listIP.append([l,ip])
	except:
		pass

import lcddriver
import time

display = lcddriver.lcd()

lcd_line = -1
try:
	if(len(listIP) > 4):
		maxRange = 4
	else:
		maxRange = len(listIP)
	for i in range (0,maxRange):
    		lcd_line = lcd_line+1 
    		display.lcd_display_string(listIP[i][0]+':'+listIP[i][1], lcd_line+1)
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
