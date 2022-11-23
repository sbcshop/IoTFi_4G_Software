'''
This is the example code for working with gsm module functionality
Develop by sbcomponents

Please make change accordinly

'''

import IoTFi_2G
import os
from IoTFi_2G import sim868, Lcd1_14
import time

LCD = Lcd1_14()#driver of lcd display

def infoDevice():
        LCD.fill(LCD.black) 
        LCD.hline(10,10,220,LCD.white)
        LCD.hline(10,125,220,LCD.white)
        LCD.vline(10,10,115,LCD.white)
        LCD.vline(230,10,115,LCD.white)       
        
        LCD.text("SB-COMPONENTS",70,40,LCD.white)
        LCD.text("IoTFi 2G",70,60,LCD.white)
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
mobile_number = "........" #Enter your mobile number whome you want to call/sms
time = 100                 #Enter time duration of your call accordingly
sms_text = "Hello from gsm test" #Enter the text you want send to 


#g = sim868().gps() #please uncomment this line for gps 


#a = sim868().call(mobile_number,time) #Please uncomment this line to call 

#m = sim868().message(mobile_number, sms_text) #Please uncomment this line for sendig txt msg
