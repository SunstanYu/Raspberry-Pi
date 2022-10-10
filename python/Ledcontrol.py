import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
try:
    for i in range (1,10):
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        time.sleep(1)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
        time.sleep(1)
except:
    print("ERROR")
GPIO.cleanup()