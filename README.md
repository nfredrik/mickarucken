***Fredrik Svärd - fs223sq***

#Overview

+++++ Give a short and brief overview of what your project is about. What needs to be included:


Tutorial on how to build a temperature and humidity sensor


The project introduces a solution how read humidity and temperature
using a a DHT11 sensor, Raspberry Pi Pico W and howto present and visulalize it
using DataCake. 




-This project introduces a solution to convert a basic humidifier into a 
-smart device, using a DHT11 sensor, Raspberry Pi Pico W, Home Assistant, 
-HiveMQ MQTT broker, Node-RED, and InfluxDB. This IoT-based automation system
-senses real-time humidity data, analyzes it and uses the information to control
-the humidifier.




This project was undertaken as part of the course 
'23ST-1DT305 Introduction to Applied IoT' at Linnaeus University, Kalmar Sweden.

All information, images, and code shared in this report are under a MIT license.


+ +++How much time it might take to do (approximation)

This project can be completed in a few hours as long as you have all 
the prerequisite software setup.

# Objective
++++Describe why you have chosen to build this specific device. What purpose does it serve? What do
++++ you want to do with the data, and what new insights do you think it will give?

#Why you chose the project
I choosen to build an application that could report humidity and temperature from garden community 
close to Brommaplan in Stockholm Sweden.
My plan was to use LoRa with either Helium or TTN as provider. It turn out that none of these providers
have coverage in this garden. My plan changed to use LoRa from my apartment since Helium have coverage
in this area.

The purpose with application was to monitor and see the temperature and humidity and se if the temperature
changes over time and and there is temperatures at the level of Frost, ie.t  temperature goes under 0 C degrees 
during spring.

-What purpose does it serve
-What insights you think it will give
I think it will be possible to get some insight on how to use LoRa and perhaps lobby for installing
a LoRa gateway in the garden community.



# Materials
-Explain all material that is needed. All sensors, where you bought them and their specifications. 
Please also provide pictures of what you have bought and what you are using.

List of material


| Enity | price |
| ----------- | ----------- |
| Bread board | 36 SEK            |
| Pico RP2 W | 36  SEK          |
| DHT11 | 36  SEK          |
| DHT11 | 36  SEK          |
| LoRa modem | 36  SEK          |
| wires | 5  SEK          |


-What the different things (sensors, wires, controllers) do - short specifications
-Where you bought them and how much they cost
-Example:

-IoT Thing	For this
-Perhaps	a table
-is a	jolly good idea?
-In this project I have chosen to work with the Pycom LoPy4 device as seen in Fig. 1, 
it's a neat little device programmed by MicroPython and has several bands of connectivity. 
The device has many digital and analog input and outputs and is well suited for an IoT project.

Image Not Showing
Possible Reasons
The image file may be corrupted
The server hosting the image is unavailable
The image path is incorrect
The image format is not supported
Learn More →
Fig. 1. LoPy4 with headers. Pycom.io

Everything purchased from electrokit.
 Comment
 Suggest edit

# Example !

Make a table?
raspberry pi pico W
The controller
Two PIR motion sensors
The sensors
LED lamp (Optional)
Used during setup as a visual rep. of the pir sensors.
Two 330ohm resistors (*For LED, also optional)
Current limiting as to protect the LED
Wire
Connecting the components
47uf Capacitor
Optional, helps stabalize the power supply to the sensors.
Bredboard (optional, you can solder if you like)



# Computer setup

++ Chosen IDE
++ How the code is uploaded
++ Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.
Putting everything together
How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. 
Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage.
Is this only for a development setup or could it be used in production?


How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware,
installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that a
beginner should be able to understand.
I have tried different type of Integrated Development Environment, IDE, like Pycharm, VScode and Thonny.
Thonny worked best when it comes to loading the target, i.e. Pico W, so I picked Thonny. The other
have better advantages when comes to supporting python.

When connecting the Pico the first time it shows up as a USB device if the push-button is actived.
To be able to load an application code the Pico W need firmware. This is easily achived by downloading
firmware from this site and that drag and drop it the the RP2 device. The firmware will be loaded
and when finished, rebooted by itself.

I use a MacOS as operating system

##Install Thonny

 ![Tux, the Linux mascot](./images/thonny.png)

To upper left indicates the folder for the files for the project. All resides
on my computer.

Th lower right you can see that the Pico W is ocnnected. The IDE detects the
target when launched. Everything is a file in Linux, that is the case for the target in this
case. It's a devicefile cu.usbmodem14201.



## Flash Micropython to Raspberry Pico W







# Circuit diagram (can be hand drawn)
-Electrical calculations

 ![Tux, the Linux mascot](./images/pico_w_layout.png)

Pins used:

 Functionality | physical pin |
| ----------- | ----------- |
| 3 Volt out | 36            |
| Ground | 38               |
| GPIO27, DHT 11 No1 | 32  |
| GPIO26, DHT 11 No2 | 31   |
| GPIO26, DHT 11 No2 | 31   |
| UART TX 0, LoRa modem | 1               |
| UART RX 0, LoRa modem | 2               |


# Platform
Describe your choice of platform. If you have tried different platforms it can be good to provide a 
comparison.

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or
a free? Describe the different alternatives on going forward if you want to scale your idea.

I choosen DataCake since it's easy and not to much work to get it going. With the measurement I 
have I think it's a goof fit.



Describe platform in terms of functionality
*Explain and elaborate what made you choose this platform
# The code
Import core functions of your code here, and don't forget to explain what you have done! Do not put
too much code here, focus on the core functionalities. Have you done a specific function that does 
a calculation, or are you using clever function for sending data on two networks? Or, are you checking
if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, 
libraries and all that is needed to understand.


# Explain your code!
Transmitting the data / connectivity
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

How often is the data sent?
Which wireless protocols did you use (WiFi, LoRa, etc …)?
Which transport protocols were used (MQTT, webhook, etc …)
*Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.
Presenting the data
Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

Provide visual examples on how the dashboard looks. Pictures needed.
How often is data saved in the database.
*Explain your choice of database.
*Automation/triggers of the data.


The file structure of the project it's simple. There is a ***main** function and number of files that
provides functionality to support the ***main** function.


| Functionality | File |
| ----------- | ----------- |
| Read temperature and humidity | temphum.py |
| Connect to a WIFI network. Source code snatched and rewritten. | wifi.py |
| Connect to a LoRa network. Source code copied and refactored to suit my means. | lora.py |
| Post data to **DataCake** | wifi.py |
| credentials for WIFI and DataCake | datacake_keys.py, keys |

````
file structure
.
├── LICENSE
├── README.md
├── lib
│   ├── datacake_keys.py
│   ├── http_requests.py
│   ├── keys.py
│   ├── lora.py
│   ├── temphum.py
│   └── wifi.py
└── main.py
````

The code have the following structure:
 - The are a setup phase, setting up WIFI, LoRA and sensors. 
 - Runtime phase where sensors are read  and posted to DataCake or some similar system. The intension is to have as much details to the the main function
as possible, **main** should deal more on behaviour.

```python
import sys
from time import sleep

from http_requests import post_values, DataCakeError
from keys import WIFI_SSID, WIFI_PASS, DEV_EUI, APP_EUI, APP_KEY
from lora import LoRa
from temphum import TempHum, get_mean_values
from wifi import Wifi

SLEEP_INTERVAL = 10
GPIO_27 = 27

def debug_print(text: str, debug=True):
    if debug:
        print(text)


def main():
    sensors = [TempHum(gpio_pin=GPIO_27),
               TempHum(gpio_pin=GPIO_27)
               ]
    wifi = Wifi(ssid=WIFI_SSID, password=WIFI_PASS)

    lora = LoRa()
    lora.setup_lora(dev_eui=DEV_EUI, app_eui=APP_EUI, app_key=APP_KEY)

    try:
        wifi.connect()
    except TimeoutError as err:
        print(f"{err}")

    while True:
        try:
            temp, hum = get_mean_values(sensors)
            debug_print(f"Temperature: {temp} C Humidity: {hum} %")
            if not wifi.connected():
                raise ConnectionDroppedError('Error, connection dropped')

            post_values(temp=temp, hum=hum)
            lora.send_over_lora(temp= temp, hum=hum )

            sleep(SLEEP_INTERVAL)

        except OSError as err:
            print(f"Problems with sensors? {err}")

        except ConnectionDroppedError as err:
            print(err)

        except DataCakeError as err:
            print(f"Failed to post{err}")

        except KeyboardInterrupt as err:
            print(f'Exiting...{err}')
            return 42


if __name__ == "__main__":
    sys.exit(main())

```
Layout  of keys.py

```python
WIFI_SSID = 'ollebollen37'
WIFI_PASS = 'chockladsanke456'

APP_EUI = "F8C83B1925EEDD37"
DEV_EUI = "F8C83B1925EEDD37"
APP_KEY = "42ED841CCD0A92561EA9ED33DF9CABBA"
```

Layout  of datacake_keys.py

```python
DATACAKE_URL = "https://api.datacake.co/integrations/api/78d4d384-d041-5bdb-af47-eb942ee19642/"
DATACAKE_SERIAL = "17ab0111-abba-4242-7117-2ea534b5c42e"

```


# Finalizing the design
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

Show final results of the project
Pictures
*Video presentation
Last changed by
T





# Wifi track

# LoRa track

My primary was to have an application using LoRa, so that was my first attempt. I started to connect
the LoRa modem and and the provided example code from the common github repo provided på LNU. I tried
a number of combination and altered the code bit by bit. I moved the application and equipment to
the roof of our buildning. In the end of the setup of the modem there is a status check checking the
modem have connected to the network. Often I got halfway, saying: "There is data sent and success", code for this 
is "03" but the status expects "There is data sent and success, there is download too.". This did never happened.
I enabled loggning the modem, and suddenly it started to work....

```python
def check_join_status(self):
        restr = ""
        self._write_cmd("AT+CSTATUS?\r\n")
        restr = self._get_response()
        if "+CSTATUS:" in restr and "08" in restr:
            return True

        return False
```
Note the credantinals are fake values
```commandline
>>> %Run -c $EDITOR_CONTENT

MPY: soft reboot
b'AT+CGMI?\r\n'b'\r\n'b'+CGMI=ASR\r\n'b'OK\r\n'
Module Connected
b'AT+CRESTORE\r\n'b'\r\n'b'OK\r\n'b'AT+ILOGLVL=1\r\n'b'\r\n'b'OK\r\n'b'AT+CSAVE\r\n'b'\r\n'b'OK\r\n'b'AT+IREBOOT=0\r\n'b'\r\n'b'OK\r\n'b'AT+CGMI?\r\n'b'\r\n'b'+CGMI=ASR\r\n'b'OK\r\n'
Module Config...
b'AT+CJOINMODE=0\r\n'b'\r\n'b'OK\r\n'
b'Ab'AT+CDEVEUI=F8C83B1925EEDD37\r\n'b'\r\n'b'OK\r\n'
b'AT+CAPPEUI=F8C83B1925EEDD37\r\n'b'\r\n'b'OK\r\n'
b'AT+CAPPKEY=42ED841CCD0A92561EA9ED33DF9CABBA\r\n'b'\r\n'b'OK\r\n'
b'AT+CULDLMODE=2\r\n'b'\r\n'b'OK\r\n'
b'AT+CCLASS=2\r\n'b'\r\n'b'OK\r\n'b'AT+CWORKMODE=2\r\n'b'\r\n'b'OK\r\n'b'AT+CDATARATE=5\r\n'b'\r\n'b'+CME ERROR:1\r\n'
Start Join.....
b'AT+CRXP=0,0,869525000\r\n'b'\r\n'b'OK\r\n'b'AT+CFREQBANDMASK=0001\r\n'b'\r\n'b'OK\r\n'b'AT+CJOIN=1,0,10,8\r\n'b'\r\n'b'OK\r\n'b'AT+CSTATUS?\r\n'b'\r\n'b'+CSTATUS:03\r\n'b'OK\r\n'
Joining....
b'AT+CSTATUS?\r\n'b'\r\n'b'+CSTATUS:03\r\n'b'OK\r\n'
Joining....
b'AT+CSTATUS?\r\n'b'\r\n'b'+CSTATUS:03\r\n'b'OK\r\n'
Joining....
b'AT+CSTATUS?\r\n'b'\r\n'b'+CSTATUS:03\r\n'b'OK\r\n'
Joining....
```

Climbed to the roof and enabled logging by the modem


```commandline
MPY: soft reboot
.
..
...
Start Join.....
b'AT+CRXP=0,0,869525000\r\n'b'\r\n'b'OK\r\n'b'AT+CFREQBANDMASK=0001\r\n'b'\r\n'b'OK\r\n'b'AT+CJOIN=1,0,10,8\r\n'b'\r\n'b'OK\r\n'b'AT+CSTATUS?\r\n'b'\r\n'b'+CSTATUS:03\r\n'b'OK\r\n'
Join success!
SENT AT+DTRX=1,1,8,ff7201a9

b'AT+DTRX=1,1,8,ff7201a9\r\n'b'\r\n'b'ERR+SEND:00\r\n'
Sent message: ff7201a9
```

 ![Tux, the Linux mascot](./images/cstatus.png)


 ![Tux, the Linux mascot](./images/datacake.png)



https://hackmd.io/@lnu-iot/iot-tutorial#How-to-write-your-tutorial
