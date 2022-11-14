from machine import Pin
import time



b1 = Pin(22, Pin.IN, Pin.PULL_UP)
b2 = Pin(23,Pin.IN, Pin.PULL_UP)

while (1):
    val1 = b1.value()
    val2 = b2.value()
    
    print("GP22 = ",val1)
    print("GP23 = ",val2)
    time.sleep(1)