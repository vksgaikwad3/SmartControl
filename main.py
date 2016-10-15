from QTouch import QTouch
from datetime import datetime
import csv


qt = QTouch()	#created instance of QTouch


devices = { 0: qt.setLoad,
	    1: qt.setLoad,
	    2: qt.setLoad,
	    3: qt.setLoad,
	    4: qt.setLoad,
	    5: qt.setLoad,
	    6: qt.setLoad,
 	    7: qt.setLoad,
	    8: qt.setLoad,
	    9: qt.setLoad,
	    10: qt.setLoad,
	    11: qt.setLoad,
	    12: qt.setLoad,
	    13: qt.setLoad,
	    14: qt.setLoad,
	    15: qt.setLoad }





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
			bitbucket[0] = int(lamp_bit[bitsize -1])
			bitbucket[1] = int(lamp_bit[bitsize -2])
			bitbucket[2] = int(lamp_bit[bitsize -3])
		if(bitsize == 6):	#0b1111 0-f
			print("Bitsize :",bitsize)
			bitbucket[0] = int(lamp_bit[bitsize -1])
			bitbucket[1] = int(lamp_bit[bitsize -2])
			bitbucket[2] = int(lamp_bit[bitsize -3])
			bitbucket[3] = int(lamp_bit[bitsize -4])
		if(bitsize == 7 ):	# Level 1 [ 0- F + Level 1 ]
			print("Bitsize : ",bitsize)
			bitbucket[0] = int(lamp_bit[bitsize -1])
			bitbucket[1] = int(lamp_bit[bitsize -2])
			bitbucket[2] = int(lamp_bit[bitsize -3])
			bitbucket[3] = int(lamp_bit[bitsize -4])
			bitbucket[4] = int(lamp_bit[bitsize -5]) # Level 1 bit
		if(bitsize == 8 ):      # Level 1 [ 0- F + Level 1 ]
			print("Bitsize : ",bitsize)
			bitbucket[0] = int(lamp_bit[bitsize -1])
			bitbucket[1] = int(lamp_bit[bitsize -2])
			bitbucket[2] = int(lamp_bit[bitsize -3])
			bitbucket[3] = int(lamp_bit[bitsize -4])
			bitbucket[4] = int(lamp_bit[bitsize -5])
			bitbucket[5] = int(lamp_bit[bitsize -6]) #Level 2 		
		if(bitsize == 9 ):
			print("Bitsize :",bitsize)
			bit_len = bitsize - 2
			#bitbucket[0] = int(lamp_bit[bitsize -1])
			#bitbucket[1] = int(lamp_bit[bitsize -2])
			#bitbucket[2] = int(lamp_bit[bitsize -3])
			#bitbucket[3] = int(lamp_bit[bitsize -4])
			#bitbucket[4] = int(lamp_bit[bitsize -5])
			#bitbucket[5] = int(lamp_bit[bitsize -6])
			#bitbucket[6] = int(lamp_bit[bitsize -7])
			no = 1
			for bit in range(0,bit_len):
				bitbucket[bit] = int(lamp_bit[bitsize - no])
				print("bit no:",bit_len)
				no += 1

		
	#print(bitbucket)
	return bitbucket



#while True:
	
#	try:
touch_status = qt.getTouchInput()  # read touch inputs Status

touch_list  = bin2list(touch_status) 
print(touch_list)

#		print ( devices[touch_status](load1 = touch_list[0],load2 = touch_list[1],load3 = touch_list[2],load4 = touch_list[3]) )

#	except KeyError:
#		print ("Key Error")
