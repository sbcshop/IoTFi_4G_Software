from machine import Pin
import time



b1 = Pin(2, Pin.IN, Pin.PULL_UP)
b2 = Pin(3,Pin.IN, Pin.PULL_UP)

while (1):
    val1 = b1.value()
    val2 = b2.value()
    
    print("GP2 = ",val1)
    print("GP3 = ",val2)
    time.sleep(1)
