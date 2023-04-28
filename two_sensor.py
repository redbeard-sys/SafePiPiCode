#authors: Nathan Hughes and Sebastian Vera
import RPi.GPIO as GPIO
import time
import datetime
import requests

headers = {"Content-Type": "application/json"}

piID = "pi0"
#GPIO pin that sensor is connected to
sensorID0 = "26"
sensorID1 = "24"

# Set up GPIO mode and pin, BCM stands for Broadcom SOC channel
GPIO.setmode(GPIO.BCM)
#utilizing raspi built in resistor on gpio pin 26
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Loop to read state of reed switch
try:
  previous_state = None

  while True:
    current_state = GPIO.input(26)
    if current_state != previous_state:
    #check whitespace
      time_stamp = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
      if current_state == False:
        print('door is closed '+str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
        #TODO
        status = '{"status": "Closed", "timestamp": "' + time_stamp + '"}'
        print(status)
        #requests.put('http://34.94.122.160:8080/api/v1/sensors/Pi0/Sen1', data=status, headers=headers)
        time.sleep(.5)
      else:
        print('door is open '+str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")))
        #TODO
        status = '{"status": "Open", "timestamp": "' + time_stamp + '"}'
        print(status)
        #requests.put('http://34.94.122.160:8080/api/v1/sensors/Pi0/Sen1', data=status, headers=headers)
        time.sleep(.5)
    previous_state = current_state
except KeyboardInterrupt:
    print("\nclean and exit program ")
    GPIO.cleanup()
