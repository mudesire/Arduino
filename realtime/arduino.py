#python -m serial.tools.list_ports Check available port
import serial
import time

def initfile(filename='temp.csv'):
	with open(filename, 'w') as f:
		f.write('"time", "distance[m]" \n')

def saveData(data):
	with open('temp.csv', 'a') as f:
		f.write(data)
		f.write('\n')

#
x_values,y_values = [], []
initfile()
#

arduino = serial.Serial('COM3',baudrate=9600, timeout=.1)  # open serial port
print(arduino.name)         # check
arduino.flush()
#
def getArduinoData(arduino):
	while True:
		try:
			data = arduino.readline().decode('ascii').strip()
			if data!='':
				timimg=time.localtime()
				timeNow='{}-{}-{}'.format(timimg.tm_hour, timimg.tm_min, timimg.tm_sec)
				y=timeNow+','+data
				#print(y)
				saveData(y)

		except KeyboardInterrupt:
			print('Keyboard Interrupt')
			arduino.close()
			break
#
getArduinoData(arduino)

