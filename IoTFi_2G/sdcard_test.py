'''
This is the example code of working with SDCard functionality of IoTFi
Developed by sbcomponents
'''

import machine
import os
import utime
import time
from IoTFi_2G import SDCard, Lcd1_14

LCD = Lcd1_14()#driver of lcd display
sd=SDCard()

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
                time.sleep(1)

infoDevice()

sd=SDCard()
vfs = os.VfsFat(sd)
os.mount(vfs, "/fc")
print("Filesystem check")
print(os.listdir("/fc")) # check the files in sd card
fn = "/fc/File.txt"
print("Single block read/write")

data = "SB COMPONENTS"
#################################################

with open(fn, "a") as f:  # append data to file
    n = f.write(data)
    print(n, "bytes written")
#################################################

#################################################
with open(fn, "r") as f:  # read data from file
    result = f.read()
    print(result)
    print(len(result), "bytes read")
os.umount("/fc")
#################################################
