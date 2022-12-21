# IoTFi-4G

IoT-Fi is a compact low power IoT enabled device having the capability of GSM module(SIM7600G-H) for providing network connectivity via using sim card and having the power of RP2040 chip. It also consists of an LCD 1.14” display, ESP32-C3, a 3.5mm jack for audio I/p - o/p, SD card and SIM card slot.

## Features:
* ESP-32(C3)
* USB type-C for power-up board and uploading codes in rp2040
* Five user Buttons
* SD card slot for storing data
* On Board RP2040
* Two antenna connectors
* A 3.5mm jack for audio input output
* 1.14 LCD display

## Features of SIM7600G-H:

* Small in size quad band (GSM/GPRS + GNSS)
* LCC + LGA form factor with abundant interfaces including UART, USB2.0, GPIO, etc.
* Low power consumption
* Embedded TCP/UDP Protocols
* LTE-FDD/LTE-TDD/UMT/UMTS/HSDPA/HSUPA/HSPA+/GSM/GPRS/EDGE
* Downlink up to 150mbps,  uplink up to 50mbps.

## LCD Features:
* 240×135 resolution, 65K RGB colors, clear and colorful displaying effect
* SPI interface, minimizes required IO pins
 
## LCD Specifications:
* Operating voltage of 3.3v/5v
* Resolution 240 x 135 pixels
* Communication Interface 4-wire SPI
* Display size of 24.91 x 14.86mm
* IPS display panel
* Pixel Size 0.1101 x 0.1035mm
* Dimension 35 x 32.00mm
 
 
 
## Hardware Overview
 Now let’s take a closer look at our IoT-Fi boards and see what other hardware components are present on it
  
 <img src ="https://github.com/sbcshop/IoTFi/blob/main/images/IotFi%204G'.png" />
 
## Downloading IDE
* To open upython(.py) files you should have Thonny IDE installed in your system, If you don’t have Thonny IDE follow the link below to install it
*  https://thonny.org/
* For brief discriptions on how to get satrt with PICO rp2040, click on link below:
https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico

## For setup the Board in thonny </b>
* Now connect USB Cable on USB Port of Pico.
* Open Thonny IDE and Choose interpreter as MicroPython (Raspberry Pi pico).

<img src="https://github.com/sbcshop/Raspberry-Pi-Pico-RFID-Expansion/blob/main/images/thonny-interpreter.PNG" />

## Working With IoTFi-4G

To start working with our this board we have provided few basics examples according to features included in this board. You can smply run the pyhon example code in your board by downloading and extracting this repository in your system. Below is the brief description of Example codes:

* Before running any example codes library file must have to save in RP2040 of your boarboard. Locate the library file under the folder ***Library*** of this repository. Open it in Thonny IDE and save it by clicking on ***file*** (Upper-left corner in your IDE) and then click on ***save a copy***, choose ***raspberry pi pico*** option enter the file name and save it as it is(do not rename).

* ***Accelerometer_Example*** this is the simple application of tilt indication in the four direction (i.e, Left, Right, Forward and , Backward). When you will upload this code in your baoard will see a ***box*** appearing according to the direction in which your board tilted. In case of no tilt it will show a message in display.

* ***GSM_Buttons_Example*** this is the example of GSM module functionality. When you will upload this code in your board you can make a call, message, and get your location by simply pressing GP buttons provided in board.

* ***SDcard_AccelerometerData.py*** this is data aquisition(gathring) from a sensor or device. In this example code you cand store the accelerometer data in SD card. Do not forget to put a sd card in it before running this example code.

* ***Wifi_Server.py*** this example code is for wiwi functionality. After connecting to any wifi network you will be able to use the wifi features of this board. 

### Note: 
Intstall the usb driver in your system(PC) provided in this repository, before using this board as a cellular via usb. After that long-press Powerkey button to activate 4G module and network led will start blinking and your system will connect to cellular.

## Documentation

* [IoTFi-4G Hardware](https://github.com/sbcshop/IoTFi-4G-Hardware)
* [Raspberry Pi Pico Getting Started with Micropython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [RP2040 Datasheet](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html)
* [Raspberry Pi Pico Datasheet](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [RP2040 Hardware Design](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [Raspberry Pi Pico Pinout](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [IoTFi-2G](https://shop.sb-components.co.uk/products/iotfi-2g-4g-iot-board-based-on-rp2040?variant=40430002307155) - Our other GSM Based product in 2G version

 ![IoTFi-2G](https://cdn.shopify.com/s/files/1/1217/2104/products/03_3.png?v=1669123121&width=400)

* [PiTalk](https://shop.sb-components.co.uk/products/pitalk-modular-smartphone-for-raspberry-pi?variant=12516562436179) - Our other GSM Based product

 ![PiTalk](https://cdn.shopify.com/s/files/1/1217/2104/products/PiTalk_-_Modular_SmartPhone_for_Raspberry_Pi_5.png?v=1528805795&width=400)

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>
