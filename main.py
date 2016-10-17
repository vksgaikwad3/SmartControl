from QTouch import QTouch
from datetime import datetime
import csv,time


qt = QTouch()	#created instance of QTouch


devices = { 0:  qt.setLoad, 1:  qt.setLoad, 2:  qt.setLoad, 3:  qt.setLoad, 4:  qt.setLoad, 5:  qt.setLoad, 6:  qt.setLoad, 7:  qt.setLoad, 8:  qt.setLoad, 9:  qt.setLoad,10:  qt.setLoad,
	    11: qt.setLoad, 12: qt.setLoad, 13: qt.setLoad, 14: qt.setLoad, 15: qt.setLoad, 16: qt.setLoad, 17: qt.setLoad, 18: qt.setLoad, 19:qt.setLoad, 20:qt.setLoad,
            21: qt.setLoad, 22: qt.setLoad, 23: qt.setLoad, 24: qt.setLoad, 25: qt.setLoad, 26: qt.setLoad, 27: qt.setLoad, 28: qt.setLoad,29:qt.setLoad, 30:qt.setLoad,
	    31: qt.setLoad, 32: qt.setLoad, 33: qt.setLoad, 34: qt.setLoad, 35: qt.setLoad, 37: qt.setLoad, 37: qt.setLoad, 38: qt.setLoad, 39:qt.setLoad, 40: qt.setLoad,
	    41: qt.setLoad, 42: qt.setLoad, 43: qt.setLoad, 44: qt.setLoad, 45: qt.setLoad, 46: qt.setLoad, 47: qt.setLoad, 48: qt.setLoad, 49: qt.setLoad, 50: qt.setLoad,
	    51: qt.setLoad, 52: qt.setLoad, 53: qt.setLoad, 54: qt.setLoad, 55: qt.setLoad, 56: qt.setLoad, 57: qt.setLoad, 58: qt.setLoad, 59: qt.setLoad, 60: qt.setLoad,
	    61: qt.setLoad, 62: qt.setLoad, 63: qt.setLoad, 64: qt.setLoad, 65: qt.setLoad, 66: qt.setLoad, 67: qt.setLoad, 68: qt.setLoad, 69: qt.setLoad, 70: qt.setLoad,
	    71: qt.setLoad, 72: qt.setLoad, 73: qt.setLoad, 74: qt.setLoad, 75: qt.setLoad, 76: qt.setLoad, 77: qt.setLoad, 78: qt.setLoad, 79: qt.setLoad, 80: qt.setLoad
	    
	   }

	



def bin2list(qt_status):

	lamp_bit = bin(qt_status)
	print ("Binary Bits:",lamp_bit)
	bitbucket = [0,0,0,0,0,0,0]	#
	bitsize = len(lamp_bit) #0b0000

	if(bitsize > 2):
	
		if(bitsize == 3):	# 0b0 0 -1 
			print ("Bitsize :",bitsize)
			bitbucket[0] = int(lamp_bit[bitsize -1]) 
		if(bitsize == 4):	# 0b00 2 - 3
			print ("Bitsize :",bitsize)
			bitbucket[0] = int(lamp_bit[bitsize -1]) # LSB D0
			bitbucket[1] = int(lamp_bit[bitsize -2]) #     D1
		if(bitsize == 5):	# 0b111 0-7
			print("Bitsize :",bitsize)
			bit_len = bitsize - 2
			no = 1
			for bit in range(0,bit_len):
				bitbucket[bit] = int(lamp_bit[bitsize - no])
				print("bit no:",bit_len)
				no += 1

		if(bitsize == 6):	#0b1111 0-f
			print("Bitsize :",bitsize)
			bit_len = bitsize - 2
			no = 1
			for bit in range(0,bit_len):
				bitbucket[bit] = int(lamp_bit[bitsize - no])
				print("bit no:",bit_len)
				no += 1
		
		if(bitsize == 7 ):	# Level 1 [ 0- F + Level 1 ]
			print("Bitsize : ",bitsize)
			bit_len = bitsize - 2
			no = 1
			for bit in range(0,bit_len):
				bitbucket[bit] = int(lamp_bit[bitsize - no])
				print("bit no:",bit_len)
				no += 1
			
		if(bitsize == 8 ):      # Level 1 [ 0- F + Level 1 ]
			print("Bitsize : ",bitsize)
			bit_len = bitsize - 2 
			no = 1
			for bit in range(0,bit_len):
				bitbucket[bit] = int(lamp_bit[bitsize - no])
				print("bit no:",bit_len)
				no += 1
		
		if(bitsize == 9 ):
			print("Bitsize :",bitsize)
			bit_len = bitsize - 2
			no = 1
			for bit in range(0,bit_len):
				bitbucket[bit] = int(lamp_bit[bitsize - no])
				print("bit no:",bit_len)
				no += 1

		
	#print(bitbucket)
	return bitbucket


#energy_usage =  "%s-%s-%s" % (datetime.now().year,datetime.now().month, datetime.now().day)
#energyAudit = 'logs/'+ energy_usage + '_Watts_consume' +.csv'

#power_usage = open(energyAudit, 'a+')	# open file in a append mode and add every new entry in new row

# Cretes a Tabs in a file which represents a Titles
#writer = csv.writer(power_usage,delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC))
#writer.writerow(('Appliance','Switch No','Appliance Rating(Watts)','ON Time','OFF Time','Total ON Time','Units Consume[kWh]'))




while True:
	
	try:
		touch_status = qt.getTouchInput()  # read touch inputs Status

		touch_list  = bin2list(touch_status) 
		print(touch_list)

		print ( devices[touch_status](load1 = touch_list[0],load2 = touch_list[1],load3 = touch_list[2],load4 = touch_list[3],
	                      level1 = touch_list[4] and  not(touch_list[5]),level2 = touch_list[5] and not(touch_list[4]), level3 =( touch_list[4] and touch_list[5] ) ,level4 = touch_list[6] ))
		time.sleep(2)
	except KeyError:
		print ("Key Error")
