'''
Name: Rohit Nachaloor
Date: 03/25/2019
Assignment No. 32
Period: 1
Cowart
'''

from EmulatorGUI import GPIO
import time
def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    print('Red LED on')
    GPIO.output(17, True)
    time.sleep(3)
    GPIO.output(17, False)
    time.sleep(1)
    print('Yellow LED on')
    GPIO.output(18, True)
    time.sleep(3)
    GPIO.output(18, False)
    time.sleep(1)
    print('Green LED on')
    GPIO.output(22, True)
    time.sleep(3)
    GPIO.output(22, False)
    time.sleep(1)
    print('Blue LED on')
    GPIO.output(23, True)
    time.sleep(3)
    GPIO.output(23, False)

if (__name__ == '__main__'):
    main()


    
