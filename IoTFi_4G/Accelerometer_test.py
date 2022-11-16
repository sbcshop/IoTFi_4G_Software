'''
This is the example code for working with accelerometer functionality of this board
Developed by sbcomponents
'''

from IOTFI_4G import IoTFi
from IOTFI_4G import accelerometer
from IOTFI_4G import Lcd1_14

axi = accelerometer()
axi.initialize()
while 1:
    x = str(axi.read_x()/2)
    y = str(axi.read_y()/2)
    z = str(axi.read_z()/2)
    print(x, y, z)
    time.sleep(0.1)
