import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.OUT,initial=GPIO.LOW)

n=0
def case0():
    pass

def case1():
    GPIO.output(17,GPIO.LOW)
    GPIO.output(22,GPIO.HIGH)

def case2():
    while n==2:
        GPIO.output(22,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(0.5)

def case3():
   GPIO.output(22,GPIO.LOW)
   GPIO.output(17,GPIO.HIGH)

def case4():
    while n==4:
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.5)

switch ={
'case0':case0,
'case1':case1,
'case2':case2,
'case3':case3,
'case4':case4,
}

def change(a):
    global n
    n=n+1
    if(n>4):
        n=1
GPIO.add_event_detect(18, GPIO.BOTH,callback=change, bouncetime=200)
while True:
    case='case'+str(n)
    switch.get(case)()
    time.sleep(0.5)


