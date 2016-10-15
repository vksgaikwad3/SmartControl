""" 
Project title : Smart Home Automation System 
Author: Vikas Gaikwad 
Company : Honey Bees Technologies Pune 
Date : 15 July 2016

Descriptions: This python file is used to set the Mode of GPIOs and to set the Directions as Input or Output 
Here we are using the Raspberry Pi Standard GPIO libray with Board pin names.

"""
import RPi.GPIO as GPIO		# GPIO control module
import time
from QTouch import QTouch

# GPIOS used in the System
L1	= 40
L2	= 38
L3	= 36
L4	= 32
Level_1 = 18
Level_2 = 22
Level_3 = 24
Level_4 = 26

# Input Pins of RF Module
RFD0	= 15
RFD1	= 23
RFD2	= 19
RFD3	= 21

# QTouch Input GPIO pins
SW_1	= 37		#LSB
SW_2	= 35
SW_3	= 33
SW_4	= 31
UP	= 29
DOWN 	= 13
FAN_CTL	= 11		#MSB

output_chanels = (L1,L2,L3,L4,Level_1,Level_2,Level_3,Level_4)
input_chanels = (SW_1,SW_2,SW_3,SW_4,UP,DOWN,FAN_CTL)

QT = QTouch()
	
# Function to gpioInit()

def gpioInit():
	
	#Set the pin modes as RpiBoard pins
	GPIO.setmode(GPIO.BOARD)
	#GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	# GPIOs used for Q-Touch inputs 
	print ("GPIOs Set")

	#output_pins =(L1,38,36,32,26,24,22)		#list of Output GPIOS used
	GPIO.setup(output_chanels,GPIO.OUT)
	GPIO.setup(output_chanels,GPIO.LOW)	# set pins LOW
	

	# GPIOs Input Pins

	GPIO.setup(input_chanels,GPIO.IN)	# set to Input
	GPIO.setup(input_chanels,GPIO.LOW)	
	
def getLoadStatus():
	
    	#output_chanels = (40,38,36,32,26,24,22)		# list of output channels
    	#output_chanels = (L1,L2,L3,L4,Level_1,Level_2,Level_3,Level_4)		# list of output channels
	outputByte = 0

	ch_size = len(output_chanels)	# size of GPIOs
	print (ch_size)

	for ch_no in range(0,ch_size):
		GPIO.setup(output_chanels[ch_no],GPIO.IN)	#set pins as input while reading their status
		print( GPIO.input(output_chanels[ch_no]))	# read pin 40 on GPIO header
		outputByte |= (GPIO.input(output_chanels[ch_no]) << ch_no)
		
	print ("OUTPUT Byte:",outputByte)
		
	print ("New Byte ****************************")	
	time.sleep(1)
	GPIO.setup(output_chanels,GPIO.OUT)		# Reset back as output 	
	
	return outputByte
	
def getTouchInput():

	''' Read Status of Touch Inputs'''
	inputByte = 0	
	#input_chanels = (SW_1,SW_2,SW_3,SW_4,UP,DOWN,FAN_CTL)
	
	input_size = len(input_chanels)

	#Create a input byte number
	
	for size in range(0,input_size):
		inputByte |= (GPIO.input(input_chanels[size])<< size)
	
	print ("INPUT Byte:", inputByte)	
	return inputByte



if __name__=='__main__':

	gpioInit()
try:
	while True:

		status = getTouchInput()
		#getLoadStatus()
		print( status )
		QT.L1_ON()
		#setLoad[status]()
		#if(status == 1):
			#GPIO.setup(L1,GPIO.OUT)
		#	GPIO.output(L1, GPIO.HIGH)
		#	print ("Set")
		#else:
		#	print ("Reset")
		#	GPIO.output(L1, GPIO.LOW)	
		
except KeyboardInterrupt:
	print ("Error Occured")
	print ("*********************** CTRL+C PRESSED ******************************************")
