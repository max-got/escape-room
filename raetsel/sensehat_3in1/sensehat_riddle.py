from sense_hat import SenseHat
import time
import random

sense = SenseHat()



def main():
	sense.set_rotation(180)
	sense.clear()
	
	stickValue = random.randint(0,8)
	
	temp = sense.get_temperature()
	tempValue = 5
	print(temp)
	
	sense.set_imu_config(False, True, False)
	gyro = sense.get_gyroscope()
	gyroValue = 2
	print(gyro["roll"])
	
	if stickValue != 5:
		stickSolved = False
	elif stickValue == 5:
		stickSolved = True
	
	tempSolved = False
	
	gyroSolved = False

	setStickBar(stickValue)
	setTempBar(tempValue)
	setGyroBar(gyroValue)
	
	while stickSolved == False or tempSolved == False or gyroSolved == False:

		for event in sense.stick.get_events():
			
			# Check if the joystick was pressed
			if event.action == "pressed":
		  
			# Check which direction and update value accordingly to call function to set the pixels
		  
				if event.direction == "up":
					if stickValue < 8:
						stickValue = stickValue + 1
						stickSolved = setStickBar(stickValue)      # Up arrow
				elif event.direction == "down":
					if stickValue > 0:
						stickValue = stickValue - 1
						stickSolved = setStickBar(stickValue)      # Down arrow
						
		if sense.get_temperature() <= temp-1:
			if tempValue > 0:
				temp = sense.get_temperature()
				tempValue = tempValue - 1
				tempSolved = setTempBar(tempValue)
			
		if sense.get_temperature() >= temp+1:
			if tempValue < 8:
				temp = sense.get_temperature()
				tempValue = tempValue + 1
				tempSolved = setTempBar(tempValue)
				
		if sense.get_gyroscope()["roll"] < 180 and sense.get_gyroscope()["roll"] > 80:
			gyroSolved = setGyroBar(0)
		
		if sense.get_gyroscope()["roll"] < 80 and sense.get_gyroscope()["roll"] > 60:
			gyroSolved = setGyroBar(1)
			
		if sense.get_gyroscope()["roll"] < 60 and sense.get_gyroscope()["roll"] > 40:
			gyroSolved = setGyroBar(2)
			
		if sense.get_gyroscope()["roll"] < 40 and sense.get_gyroscope()["roll"] > 20:
			gyroSolved = setGyroBar(3)
			
		if sense.get_gyroscope()["roll"] < 20 and sense.get_gyroscope()["roll"] > 0:
			gyroSolved = setGyroBar(4)
		
		if sense.get_gyroscope()["roll"] < 360 and sense.get_gyroscope()["roll"] > 340:
			gyroSolved = setGyroBar(5)
			
		if sense.get_gyroscope()["roll"] < 340 and sense.get_gyroscope()["roll"] > 320:
			gyroSolved = setGyroBar(6)
			
		if sense.get_gyroscope()["roll"] < 320 and sense.get_gyroscope()["roll"] > 300:
			gyroSolved = setGyroBar(7)
			
		if sense.get_gyroscope()["roll"] < 300 and sense.get_gyroscope()["roll"] > 280:
			gyroSolved = setGyroBar(8)
			
		if sense.get_gyroscope()["roll"] < 280 and sense.get_gyroscope()["roll"] > 180:
			gyroSolved = setGyroBar(8)
		
		#print(sense.get_temperature())
		#print(sense.get_gyroscope())
			
	solved()
	
def solved():
	for i in range(0,3):
		setStickBar(0)
		setTempBar(0)
		setGyroBar(0)
		time.sleep(.3)
		setStickBar(5)
		setTempBar(3)
		setGyroBar(6)
		time.sleep(.3)
	return True
		
	
	
def setStickBar(stick):
	clearBar(0, 2)
	#print("Update: " + str(stick))
	for y in range(0,stick):
		for x in range(0,2):
			if stick == 5:
				sense.set_pixel(x, y, (0, 255, 0))
			else:
				sense.set_pixel(x, y, (255, 0, 0))
	if stick == 5:
		return True
	else:
		return False
				
def setTempBar(temp):
	clearBar(3, 5)
	for y in range(0,temp):
		for x in range(3,5):
			if temp == 3:
				sense.set_pixel(x, y, (0, 255, 0))
			else:
				sense.set_pixel(x, y, (255, 0, 0))
	if temp == 3:
		return True
	else:
		return False
				
def setGyroBar(gyro):
	clearBar(6, 8)
	for y in range(0,gyro):
		for x in range(6,8):
			if gyro == 6:
				sense.set_pixel(x, y, (0, 255, 0))
			else:
				sense.set_pixel(x, y, (255, 0, 0))
	if gyro == 6:
		return True
	else:
		return False
				
				
def clearBar(x1,x2):
	for y in range(0, 8):
		for x in range(x1,x2):
			sense.set_pixel(x, y, (0, 0, 0))
			
#main()

	

