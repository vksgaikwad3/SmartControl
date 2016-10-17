''' This script will deal with controlling lights as per QTouch inputs

'''

import time
from datetime import datetime
import RPi.GPIO as GPIO
import numpy


# GPIOS used in the System
L1      = 40
L2      = 38
L3      = 36
L4      = 32
Level_1 = 18
Level_2 = 22
Level_3 = 24
Level_4 = 26

# Input Pins of RF Module
RFD0    = 15
RFD1    = 23
RFD2    = 19
RFD3    = 21

# QTouch Input GPIO pins
SW_1    = 37            #LSB
SW_2    = 35
SW_3    = 33
SW_4    = 31
UP      = 29
DOWN    = 13
FAN_CTL = 11            #MSB



output_chanels = (L1,L2,L3,L4,Level_1,Level_2,Level_3,Level_4)
input_chanels = (SW_1,SW_2,SW_3,SW_4,UP,FAN_CTL,DOWN)




class QTouch:
		
	d1flage = 0
	prev_val = 0
	T1on = T1off = total1 = 0
	
	def __init__(self):
		
	        ''' Constructor will set GPIOs modes'''
		#Set the pin modes as RpiBoard pins
	        GPIO.setmode(GPIO.BOARD)
        	GPIO.setwarnings(False)
        	# GPIOs used for Q-Touch inputs 
        	print ("GPIOs Set")

        	#output_pins =(L1,38,36,32,26,24,22)            #list of Output GPIOS used
        	GPIO.setup(output_chanels,GPIO.OUT)
        	GPIO.setup(output_chanels,GPIO.LOW)     # set pins LOW

        	# GPIOs Input Pins

        	GPIO.setup(input_chanels,GPIO.IN)       # set to Input
        	GPIO.setup(input_chanels,GPIO.LOW)


	def getLoadStatus(self):
	
        	outputByte = 0

        	ch_size = len(output_chanels)   # size of GPIOs
        	print (ch_size)

        	for ch_no in range(0,ch_size):
        	        GPIO.setup(output_chanels[ch_no],GPIO.IN)       #set pins as input while reading their status
                	print( GPIO.input(output_chanels[ch_no]))       # read pin 40 on GPIO header
                	outputByte |= (GPIO.input(output_chanels[ch_no]) << ch_no)

	        print ("OUTPUT Byte:",outputByte)

        	print ("New Byte ****************************")
        	time.sleep(1)
        	GPIO.setup(output_chanels,GPIO.OUT)             # Reset back as output  

        	return outputByte

	def getTouchInput(self):

        	''' Read Status of Touch Inputs'''
        	inputByte = 0

        	input_size = len(input_chanels)

        	#Create a input byte number

        	for size in range(0,7):
                	inputByte |= (GPIO.input(input_chanels[size])<< size)

        	print ("INPUT Byte DEC: %d  HEX : %x" %(inputByte,inputByte))
        	return inputByte

	
        # Functions to control the loads		
	def Load_1(self,value):
		
		print("Preveious Value:",self.prev_val)
		print("dflage Value :", self.d1flage)
		try:
			if(self.prev_val == 0 and value == 1):	#device ON 
				GPIO.output(L1,value)
				print("L1_1:",value)
				print("In OFF - ON  State ")
				self.T1on = datetime.now()
				print("ON Time:",self.T1on)
				self.d1flage = 1			# flage to detect from ON to OFF transition
				self.prev_val = value
					

			elif(self.prev_val == 1 and self.d1flage == 1 and value == 0):	# ON - OFF
				GPIO.output(L1,value)
				print("In ON - OFF ")
				self.d1flage = 0
				self.T1off = datetime.now()
				print("OFF Time:",self.T1off)
				self.total1 = self.T1off - self.T1on
				print("Total Time :",self.total1)

			elif(self.d1flage == 0 and value == 0):	# default OFF state
				print ("Default OFF State")
				GPIO.output(L1,value)

		finally:
			self.prev_val = value
			print("Finally Prev_val:",self.prev_val)
			return value		
							
		
		
	def Load_2(self,value):
		GPIO.output(L2,value)
		print("L2:",value)
		return value
		
	def Load_3(self,value):
		GPIO.output(L3,value)
		print("L3:",value)
		return value
	
	def Socket(self,value):
		GPIO.output(L4,value)
		print("L4:",value)
		return value

		

	def Fan_Control(self,level1 = 0,level2 = 0,level3 = 0,level4=0):
		# This Method will set the Fan Levels
		
		GPIO.output(Level_1,level1)
		GPIO.output(Level_2,level2)
		GPIO.output(Level_3,level3)
		GPIO.output(Level_4,level4)


	def Master_Control(self,value):
		
		self.Load_1(value)
		self.Load_2(value)
		self.Load_3(value)
		self.Socket(value)
		self.Fan_Control(level1 = value, level2 = 0, level3 = 0, level4 = 0)

	def setLoad(self,load1 = 0,load2 = 0,load3 = 0,load4 = 0,level1 = 0,level2 = 0,level3 = 0,level4 = 0):

                self.Load_1(load1) 
                self.Load_2(load2)
                self.Load_3(load3)
                self.Socket(load4)
                self.Fan_Control(level1,level2,level3,level4)

	

if __name__=='__main__':

	qt = QTouch()
	qt.setLoad(load1=0,load2=1)
