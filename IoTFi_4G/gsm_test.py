'''
This is the example code for working with gsm module functionality
Develop by sbcomponents

Please make changes accordingly
'''

import IoTFi_2G
import os
from IOTFI_4G import IoTFi, Lcd1_14
import time

LCD = Lcd1_14()#driver of lcd display

def infoDevice():
        LCD.fill(LCD.black) 
        LCD.hline(10,10,220,LCD.white)
        LCD.hline(10,125,220,LCD.white)
        LCD.vline(10,10,115,LCD.white)
        LCD.vline(230,10,115,LCD.white)       
        
        LCD.text("SB-COMPONENTS",70,40,LCD.white)
        LCD.text("PICO 4G",70,60,LCD.white)
        LCD.text("EXPANSION",70,80,LCD.white)  
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
                time.sleep(1)

infoDevice()
mobile_number = "9118520507"
time = 100
sms_text = "Hello from gsm test"


#Message = IoTFi().message(Mobile_number,Write_message) #send the message

#Call = IoTFi().call(Mobile_number,60) # uncomment this to make call 60 means duration of call(you can change according to you)

#Gps = IoTFi().gps() #uncomment this to use gps

