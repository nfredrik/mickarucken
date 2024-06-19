Tutorial on how to build a temperature and humidity sensor
Give a short and brief overview of what your project is about. What needs to be included:

# Kyrksjölötens gardening monitoring

Fredrik Svärd - fs223sq

Short project overview

The project introduces a solution how read humidity and temperature
using a a DHT11 sensor, Raspberry Pi Pico W and present and visulalize
data using ada fruit. 

#This project introduces a solution to convert a basic humidifier into a 
#smart device, using a DHT11 sensor, Raspberry Pi Pico W, Home Assistant, 
#HiveMQ MQTT broker, Node-RED, and InfluxDB. This IoT-based automation system
#senses real-time humidity data, analyzes it and uses the information to control
#the humidifier.

This project was undertaken as part of the course 
'23ST-1DT305 Introduction to Applied IoT' at Linnaeus University, Kalmar Sweden.

All information, images, and code shared in this report are under a MIT license.


How much time it might take to do (approximation)

This project can be completed in a few hours as long as you have all 
the prerequisite software setup.

# Objective
#Describe why you have chosen to build this specific device. What purpose does it serve? What do you want to do with the data, and what new insights do you think it will give?

#Why you chose the project
I choosen to build an application that could report humidity and temperate from garden close to Brommaplan.
My plan was to use LoRa with either Helium or TTN as provider. It turn out that none of these providers
have coverage in this garden. My plan changed to use LoRa from my apartment since Helium have coverage
in this area.

The purpose with application was to monitor and see the temperature and humidity and se if the temperature
goes under 0 degrees Celius during spring.
#What purpose does it serve
#What insights you think it will give
I think it will be possible to get some insight on how to use LoRa and perhaps lobby for installing
a LoRa gateway in the garden community.

My primary was to have an application using LoRa, so that was my first attempt. I started to connect
the LoRa modem and and the provided example code from the common github repo provided på LNU. I tried
a number of combination and altered the code bit by bit. I moved the application and equipment to
the roof of our buildning. In the end of the setup of the modem there is a status check checking the
modem have connected to the network. Often I got halfway, saying: "Data message sent", code for this 
is "03" but the status expects "Data message sent and download link active". This did never happened.
I enabled loggning the modem, and suddenly it started to work....

# Material
#Explain all material that is needed. All sensors, where you bought them and their specifications. 
Please also provide pictures of what you have bought and what you are using.

List of material

#What the different things (sensors, wires, controllers) do - short specifications
#Where you bought them and how much they cost
#Example:

#IoT Thing	For this
#Perhaps	a table
#is a	jolly good idea?
#In this project I have chosen to work with the Pycom LoPy4 device as seen in Fig. 1, 
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

# Computer setup
How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware,
installing plugins in your favorite editor. How flashing is done on MicroPython. The aim is that a
beginner should be able to understand.

# Chosen IDE
How the code is uploaded
Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.
Putting everything together
How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. 
Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage.
Is this only for a development setup or could it be used in production?

# Circuit diagram (can be hand drawn)
*Electrical calculations

# Platform
Describe your choice of platform. If you have tried different platforms it can be good to provide a 
comparison.

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or
a free? Describe the different alternatives on going forward if you want to scale your idea.

Describe platform in terms of functionality
*Explain and elaborate what made you choose this platform
# The code
Import core functions of your code here, and don't forget to explain what you have done! Do not put
too much code here, focus on the core functionalities. Have you done a specific function that does 
a calculation, or are you using clever function for sending data on two networks? Or, are you checking
if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, 
libraries and all that is needed to understand.








import this as that

def my_cool_function():
    print('not much here')

s.send(package)

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

# Finalizing the design
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

Show final results of the project
Pictures
*Video presentation
Last changed by  
 
T

https://hackmd.io/@lnu-iot/iot-tutorial#How-to-write-your-tutorial
