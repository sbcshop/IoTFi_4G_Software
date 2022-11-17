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
 Now let’s take a closer look at our IoT-Fi board and see what other hardware components are on it
 
## Downloading IDE
* To open upython(.py) files you should have Thonny IDE installed in your system, If you don’t have Thonny IDE follow the link below to install it
*  https://thonny.org/
* For brief discriptions reagrding how to satrt with PICO RP2040, click on link below
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

* Step.5 - Ater saving the liberary file you can pick any example file to test your board, and start working as your wish by some modifications(if require) accordingly.

