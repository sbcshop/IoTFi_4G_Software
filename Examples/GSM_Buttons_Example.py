'''
#------------------------------------------------------------------------
#
# This is a python Example code for IoTFi-4G Board
# Written by SB Components Ltd 
#
#==================================================================================
# Copyright (c) SB Components Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
'''

from machine import Pin
import os
from IoTFi_4G import IoTFi, Lcd1_14
import time

LCD = Lcd1_14()#driver of lcd display

def infoDevice():
        LCD.fill(LCD.black) 
        LCD.hline(10,10,220,LCD.white)
        LCD.hline(10,125,220,LCD.white)
        LCD.vline(10,10,115,LCD.white)
        LCD.vline(230,10,115,LCD.white)       
        
        LCD.text("SB-COMPONENTS",70,40,LCD.white)
        LCD.text("IoTFi 4G",70,60,LCD.white)
        LCD.lcd_show()
        time.sleep(2)
        LCD.fill(LCD.black)
        LCD.text("WAITING.....",70,40,LCD.white)
        LCD.lcd_show()
        x = 0
        for y in range(0,1):
                x += 4
                LCD.text(".",125+x,40,LCD.white)
                LCD.lcd_show()
                time.sleep(2)
                LCD.fill(LCD.black)

infoDevice()

mobile_number = "Enter your mobile number"
time = 100
sms_text = "Hello from gsm test"

b1 = Pin(22, Pin.IN, Pin.PULL_UP)
b2 = Pin(23,Pin.IN, Pin.PULL_UP)

val1 = b1.value()
val2 = b2.value()

print("Press GP22 button to send message")
print("Press GP23 button to call")

    
while True:
    if b1.value() == 0:
        print("Sending msg....")
        LCD.text("Sending...",70,40,LCD.white)
        LCD.lcd_show()
        Message = IoTFi().message(mobile_number,sms_text)
        break
    
    if b2.value() == 0:
        print("Calling....")
        LCD.text("Calling...",70,40,LCD.white)
        LCD.lcd_show()
        Call = IoTFi().call(mobile_number,time)
        break
    if b2.value() == 0 and b1.value() == 0:
        print("Getting Location")
        LCD.text("Locating...",70,40,LCD.white)
        LCD.lcd_show()
        Gps = IoTFi().gps()
        break

