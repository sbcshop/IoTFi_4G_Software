import IoTFi_2G
from IoTFi_2G import accelerometer
import time

axi = accelerometer()
axi.initialize()
while 1:
    x = str(axi.read_x()/2)
    y = str(axi.read_y()/2)
    z = str(axi.read_z()/2)
    print(x, y, z)
    time.sleep(0.1)
