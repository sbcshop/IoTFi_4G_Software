# IoT-Fi

IoT-Fi is a compact low power IoT enabled device having the capability of GSM modules (SIM868/SIM7600G-H) for providing network connectivity via using sim card and having the power of RP2040 chip. It also consists of an LCD 1.14” display, ESP32-C3, a 3.5mm jack for audio I/p - o/p, SD card and SIM card slot.

## Features:
* ESP-32(C3)
* USB type-C for power-up board and uploading codes in rp2040
* Five user Buttons
* SD card slot for storing data
* On Board RP2040
* Two antenna connectors
* A 3.5mm jack for audio input output
* 1.14 LCD display

# Features of SIM Modules

## Features of SIM868:

* Small in size quad band (GSM/GPRS + GNSS)
* LCC + LGA form factor with abundant interfaces including UART, USB2.0, GPIO, etc.
* Low power consumption
* Embedded TCP/UDP Protocols

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

## Steps To Follow for Working with IoT-Fi Boards
After downloading and installing thonny ide you will able to run our example codes in IoTFi boards, for this please follow the steps below:

* Step.1 - Download the Zip file of IoTFi package and extract it in your computer system, for this click on code—>download Zip

* Step.2 - After downloading and extrating the Zip file of this package you will get two different directries i.e, "IoTFi_2G" and "IoTFi_4G" for working with our 2G and 4G boards.

* Step.3 - If you wont to work with our 2G module, open the IoTFi_2G directory you can see here multiple python files in this folder.

* Step.4 - The file named with "IoTFi_2g" is the liberary file, you should have to save this file in rp2040 of our boards by naming as it is

* Step.5 - Ater saving the liberary file you can pick any example file and put a suitable sim card in simslot to test your board, and start working as you want by some modifications(if require) in the code.

### Note: 
Intstall the usb driver provide in "IoTFi-4G" directory in your system(PC) before using it as a cellular via usb. After that long-press Powerkey button to activate 4G module and network led will start blinking and your system will connect to cellular.

## Documentation

* [IoTFi-2G Software](https://github.com/sbcshop/IoTFi_2G_Software)
* [Raspberry Pi Pico Getting Started with Micropython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [RP2040 Datasheet](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html)
* [Raspberry Pi Pico Datasheet](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [RP2040 Hardware Design](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
* [Raspberry Pi Pico Pinout](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Related Products

* [IoTFi-4G](https://shop.sb-components.co.uk/products/iotfi-2g-4g-iot-board-based-on-rp2040?variant=40430002307155) - Our other GSM Based product in 4G version

 ![IoTFi-4G](https://cdn.shopify.com/s/files/1/1217/2104/products/Untitled-2.png?v=1669123121&width=300)


## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more informnation.

Please contact [support@sb-components.co.uk](support@sb-components.co.uk) for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>
