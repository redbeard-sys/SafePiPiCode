import RPi.GPIO as GPIO
import time
import datetime

# Set up GPIO mode and pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Loop to read state of reed switch
try:
  previous_state = None

  while True:
    current_state = GPIO.input(26)
    if current_state != previous_state:
      if current_state == False:
        print('door is closed '+str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        time.sleep(.5)
      else:
        print('door is open '+str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        time.sleep(.5)
    previous_state = current_state
except KeyboardInterrupt:
    print("\nclean and exit program ")
    GPIO.cleanup()
