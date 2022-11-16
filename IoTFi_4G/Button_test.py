'''
This is the example code for working with additional GPIO's  functionality
Developed by sbcomponents

'''

from machine import Pin
import time


b1 = Pin(22, Pin.IN, Pin.PULL_UP)
b2 = Pin(23,Pin.IN, Pin.PULL_UP)

GP15 = Pin(15,Pin.OUT)
GP26 = Pin(26,Pin.OUT)
while (1):
    GP15.value(1)
    GP26.value(1)
    
    val1 = b1.value()
    val2 = b2.value()
    
    print("GP22 = ",val1)
    print("GP23 = ",val2)
    time.sleep(1)
