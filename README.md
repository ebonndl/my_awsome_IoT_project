By Bongani Ndlovu, (bn222if)
# Table of Contents
[TOC]
## Description

In this tutorial, you will learn how to build a temperature, humidity, and water level monitoring system using [Raspberry Pi Pico W](#2-Raspberry-Pi-Pico-W-Pinout-diagram), a DHT11 sensor will measure temperature and humidity, a water level sensor will be used to monitor the amount of water. 
The system utilizes Docker to log and share sensor data on a Raspberry Pi, with the following components:
* Mosquitto: Message broker for data communication.
* InfluxDB: Database for storing sensor data.
* Node-RED: Data bridge for processing and routing data.
* Grafana: Visualization tool for displaying sensor data.

Additionally, the system incorporates an OLED display, RGB LED, and Buzzer for local visualization and alert notifications.

#### Time Allocation
The assembly and coding process for this tutorial can generally be completed within a reasonable timeframe of approximately 1-2 hours. However, it's important to consider personal preferences in terms of data visualization choices and the time needed to become familiar with the components and tools used in the project.

Here's a breakdown of the time allocation for each step:

##### 1. Preparing Raspberry Pi Pico W and connecting the components:
* This step typically takes around 30 minutes to 1 hour, depending on your familiarity with the hardware and breadboard connections.

##### 2. Writing the code:
* The provided code is ready to use, but understanding it and making any necessary modifications or customizations may require around 1-2 hours for an average beginner.

##### 3. Setting up the Raspberry Pi to host the required services:
* This step involves installing and configuring Docker, Portainer, Mosquitto MQTT broker, Node-RED, InfluxDB and Grafana on the Raspberry Pi.
* On average, an additional 1-2 hours for an average beginner will be required to complete this setup. The actual time required may vary based on your familiarity with the tools and the complexity of the setup.

Please note that these time estimates are approximate and can vary depending on individual experience, learning speed, and familiarity with the tools and concepts involved. It's always recommended to allocate some extra time for troubleshooting and debugging, as unforeseen challenges may arise during the process.

## Goal and Objective

The goal of this tutorial is to guide you through the process of enhancing an existing egg incubator by implementing a remote climate monitoring system. With this system, you will be able to monitor the climate conditions inside the incubator remotely, even when you are away. The focus of the monitoring system will be on temperature, humidity, and water level, as these factors play a crucial role in the hatching process.

#### Background
Maintaining optimal conditions is crucial for successful hatching in an incubator. Proper egg rotation, accurate temperature, and humidity levels are essential factors. While the incubator's built-in motor handles the rotation, this tutorial focuses on monitoring temperature, humidity, and water level.

These are the required temperature and humidity tolerances:

| Period | Temperature | Humidity |
| ------ | ----------- | -------- |
| First 18 days| 37.7 °C | 57%    |
| Last 3 days of the 21 days | 36.9 °C     | 70%  |

##### Understanding the relationship between water, temperature, and humidity

To successfully maintain the desired humidity levels, it is important to understand how water, temperature, and humidity influence each other in the incubator:

1. Water Evaporation:

    The presence of water in the incubator leads to evaporation, increasing the moisture content in the air and raising the humidity level.
    Conversely, if there is less water available, evaporation decreases, resulting in lower humidity levels.

2. Temperature:

    Temperature plays a significant role in humidity levels as well.
    Warmer temperatures accelerate evaporation, leading to higher humidity levels.
    On the other hand, lower temperatures slow down evaporation, resulting in reduced humidity levels.

By comprehending this relationship, you will be able to make informed decisions and adjustments to maintain the appropriate humidity levels in the incubator.

## Material

The selection of materials can be tailored according to the user's preferences, and it is recommended to refer to the equipment datasheets for comprehensive specifications and details of the individual components.

|#|Preview|Item|Description|Approximate price|
| --- | -------- | ------ | ------ | -------- |
| 1.  | ![](https://hackmd.io/_uploads/B1Sczwvun.jpg) | 1 x [Raspberry Pi Pico W](https://www.electrokit.com/produkt/raspberry-pi-pico-w/?gclid=EAIaIQobChMItKbR_tzl_wIVcuTmCh3C4A1tEAAYAiAAEgIIqPD_BwE), with pre-soldered 40-pin header and micro USB-USB-A Cable | The Raspberry Pi Pico W microcontroller board acts as the project's central component. It handles sensor data collection, monitoring logic execution, and facilitates communication with other system components.  | 138.00 SEK |
| 2.  | ![](https://hackmd.io/_uploads/HyWafwP_h.jpg) | 1 x [DHT11 Sensor](https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/) – Temperature and humidity sensor. | The DHT11 sensor measures temperature (0-50°C) and humidity (20-80%) with respective accuracies of 2 degrees and 5%. It has a sampling rate of 1Hz, operating at 3-5V with a maximum current of 2.5mA. | 78.00 SEK  |
| 3.  | ![](https://hackmd.io/_uploads/rJ_kQvw_3.jpg) | 1 x [Water level sensor](https://www.fruugo.se/5-pieces-rain-water-sensor-liquid-level-sensor-rain-water-detection-for-detection-area-40mmx16mm/p-119987351-252224651?language=en&ac=ProductCasterAPI&asc=pmax&gclid=EAIaIQobChMIm9uHyN_l_wIV2fhRCh2aAwAUEAQYDCABEgJ_oPD_BwE) | The water level sensor converts analog signals for direct microcontroller reading. It uses parallel wires to measure drops and determine water level. Operating range: temperature (10-30°C), humidity (10-90%), voltage (3-5V), current (<20mA), detection area (40mm x 16mm). | 132.00 SEK (5pcs) |
| 4.  | ![](https://hackmd.io/_uploads/rysZmPw_3.jpg) | 1 x [OLED Display](https://www.amazon.se/AZDelivery-I2C-Skärm-kompatibel-Raspberry-inklusive/dp/B01L9GC470/ref=asc_df_B01L9GC470/?tag=shpngadsglede-21&linkCode=df0&hvadid=476458655005&hvpos=&hvnetw=g&hvrand=2169706603414924&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012324&hvtargid=pla-402608082122&psc=1) | The compact 0.96" OLED display has a vibrant 128x64 blue pixel screen. It provides a clear visual interface to display real-time information like temperature, humidity, and water level readings. | 77.00 SEK |
| 5.  | ![](https://hackmd.io/_uploads/BymEmvvd2.jpg) | 1 x [RGB LED SMD](https://www.electrokit.com/produkt/led-modul-rgb-smd/) | The KY-009 SMD Module LED RGB 3 Full Color consists of three compact RGB LEDs. It offers colorful visual indicators for different system states in the tutorial.| 116.00 SEK |
| 6.  | ![](https://hackmd.io/_uploads/rkFLQwPuh.jpg) | 1 x [Buzzer](https://www.electrokit.com/produkt/piezohogtalare-passiv/) | The passive piezo buzzer module is a small audio device that generates sound when an electrical signal is applied. It adds audible alerts to the project, indicating specific events or conditions.| 68.00 SEK |
| 7.  | ![](https://hackmd.io/_uploads/ryytXvw_n.jpg) | Jumper wires and 3 x [mini breadboards](https://www.amazon.se/AZDelivery-Breadboard-Kit-Bygelkabel-kompatibel/dp/B07NJ3FX25/ref=sr_1_4?crid=34VBKF5QMOFDY&keywords=3%2Bx%2Bmini%2Bbreadbord&qid=1687948256&sprefix=3%2Bx%2Bmini%2Bbreadbord%2Caps%2C220&sr=8-4&th=1) | Jumper wires and mini breadboards are versatile connectors used in electronics projects to establish component connections. They offer a flexible and convenient way to link circuit parts, enabling easy prototyping. With different lengths and colors available, jumper wires provide flexibility in organizing and routing connections.|111.00 SEK|
|  |       |     |Total:|714.00 SEK|

## Preparation
#### 1. Download and Install Thonny IDE:
* Visit the Thonny IDE website at https://thonny.org/ and download the appropriate version for your operating system.
* Follow the installation instructions provided on the website to install Thonny IDE on your computer.

#### 2. Raspberry Pi Pico W Firmware Installation:
1. Download the Raspberry Pi Pico W firmware from [here](https://projects.raspberrypi.org/en/projects/get-started-pico-w/1)
2. Locate the downloaded .uf2 firmware file, typically in the "Downloads" folder. The current firmware version is rp2-pico-w-20230426-v1.20.0.uf2.
3. Connect the Micro USB end of the cable to your Raspberry Pi Pico W before connecting it to your computer.
4. Press and hold the BOOTSEL button on your Raspberry Pi Pico W.
5. While holding the BOOTSEL button, connect the USB-A or USB-C end of the cable to your computer.
6. Your file manager should open, displaying the Raspberry Pi Pico as an external drive.
7. Drag and drop the downloaded .uf2 firmware file into the file manager window.
8. The Raspberry Pi Pico will disconnect, and the file manager window will close.

#### 3. Using Thonny Editor:
* Launch the Thonny editor, which you installed in the previous step.
* At the bottom right-hand corner of the Thonny editor, you will see some text indicating the currently selected Python version.
* If it does not display "MicroPython (Raspberry Pi Pico)" and COM port, click on the text and select "MicroPython (Raspberry Pi Pico)" from the available options. ![Image 1](https://hackmd.io/_uploads/r1n4LOuu2.png)

#### 4. Installing Libraries using Thonny Editor:
   * Launch the Thonny editor, which you installed in the previous step.
   * Ensure that "MicroPython (Raspberry Pi Pico)" is selected at the bottom right-hand corner of the Thonny editor. 
    * Navigate to the Thonny Tools Menu (#*1.*) > Manage packages...(#*2.*)
     ![Image 2](https://hackmd.io/_uploads/HyR7KO_u3.png)
   * In the popup menu, type the name of the library you want to install into the search field (#*3.*) and Click Search on PyPI (#*4.*). ![Image 3](https://hackmd.io/_uploads/rkv1nO_d3.png)
   * Select the appropriate library from the search results.
   * Click the Install button (#*5.*) at the bottom of the menu to begin the installation process.
   * Wait for the installation to complete. You will see a progress bar indicating the installation progress.
   * Once the installation is finished, you will be prompted to close the package manager. 
   * Click the Close button (#*6.*) to exit the package manager.

#### 5. Raspberry Pi IoT Server Setup:
If you want to learn how to set up your own Raspberry Pi IoT server with MQTT, Node-RED, InfluxDB, and Grafana, you can follow this link: https://learnembeddedsystems.co.uk/easy-raspberry-pi-iot-server. 
The provided guide includes a comprehensive video tutorial that offers step-by-step instructions to help you set up the server and establish data connectivity.

These steps will prepare your system and Raspberry Pi Pico W for the subsequent stages of the tutorial.

## Hardware connection
#### 1. Component Wiring Instructions for Raspberry Pi Pico W:
1.1. Connecting Water Level Sensor:

| Raspberry Pi Pico W | Water Level Sensor |
| ------------------- | --------|
| 3V3(OUT)            | VCC pin |
| Any ground (GND)    | GND pin |
| ADC(2) pin (Pin 28) | OUT pin |
   
1.2. Connecting DHT11 Sensor:

| Raspberry Pi Pico W| DHT11 sensor |
| ----------------- | -------- |
| 3V3(OUT)          | VCC pin  |
| Any ground (GND)  | GND pin  |
| GP22 pin (Pin 22) | DATA pin |
    
1.3. Connecting RGB LED:
| Raspberry Pi Pico W | RGB module |
| ------------------- | --------   |
| Any ground GND | Minus pin  |
| GPIO (Pin 2)   | blue_led   |
| GPIO (Pin 3)   | red_led    |
| GPIO (Pin 4)   | green_led  |

1.4. Connecting Buzzer:
| Raspberry Pi Pico W | Buzzer module |
| ------------------- | ------------- |
| 3V3(OUT)         | VCC pin    |
| Any ground (GND) | Minus pin  |
| GPIO (Pin 4)     | Output pin |

1.5. Connecting OLED Display (I2C Interface):
| Raspberry Pi Pico W | OLED display |
| --------         | --------|
| 3V3(OUT)         | VCC pin |
| Any ground (GND) | GND pin |
| SDA (Pin 26) | SDA pin |
| SCL (Pin 27) | SCL pin |

By following these wiring instructions, you will establish the necessary electrical connections between the components and the Raspberry Pi Pico W, allowing them to communicate and interact effectively.

#### 2. Raspberry Pi Pico W Pinout diagram
![](https://hackmd.io/_uploads/B1nDicD_2.png)

#### 3. Circuit diagram/ Component assembly:
   Note that actual components may differ from the ones shown in the example, 
    but the general principles of connection remain the same.
![](https://hackmd.io/_uploads/SJACbqPun.png)

## Code and Prerequisites for Running the code

To run the code for this project, you will need the following prerequisites:

#### 1. MicroPython Firmware:
Ensure that you have flashed the MicroPython firmware onto your Raspberry Pi Pico W, as described in the ["Preparation"](#Preparation) section of this tutorial.

#### 2. Required Libraries: 
Install the necessary libraries to your Raspberry Pi Pico W by following the steps provided in the ["Installing Libraries using Thonny Editor"](#4-Installing-Libraries-using-Thonny-Editor:) section of this tutorial.
  * The following two libraries needs to be installed by follow the above mentioned steps;
    1. umqtt.simple: This library provides a simple MQTT client implementation for MicroPython.
    2. ssd1306: This library allows you to communicate with SSD1306-based OLED displays.
* In addition to the two libraries (i.e. *umqtt.simple* and *ssd1306*), the following libraries are part of the MicroPython standard library and should already be available on your Raspberry Pi Pico W. They can be directly import them into the project:
    1. utime: Provides functions for working with time and delays.
    2. ubinascii: Provides functions for working with binary and ASCII data.
    3. ujson: Provides functions for working with JSON data.
    4. machine: Provides access to various hardware components and interfaces on the microcontroller.
    5. dht: Allows interaction with DHT series temperature and humidity sensors.
    6. network: Provides network-related functions and classes, such as connecting to Wi-Fi networks.
    7. boot: This is a custom module specific to your project. Ensure you have the boot.py file available.
    
#### 3. Downloading the Code: 
   * The complete code, including the required libraries, can be downloaded from my GitHub repository. You can access the code from the following link: [myGitHubRepository](https://github.com/ebonndl/my_awsome_IoT_project).
   * Once you have downloaded the code, make sure to extract it to a convenient location on your computer.
   
#### 4. Uploading the Code: 
   To upload the code to your Raspberry Pi Pico W, follow the steps below:
1. Connect your Raspberry Pi Pico W to your computer using a Micro USB cable.
2. Launch the Thonny editor, which you installed during the preparation process.
3. Make sure "MicroPython (Raspberry Pi Pico)" is selected as the Python version and the correct COM port is selected in the bottom right-hand corner of the Thonny editor.
4. Open the main code file (e.g., main.py) from the extracted code folder in Thonny.
5. Click the "Run" button or press F5 to upload and run the code on your Raspberry Pi Pico W.

By following these steps and ensuring that you have the necessary firmware, libraries, and code, you will be able to successfully run the project code on your Raspberry Pi Pico W.

#### 5. Code snippet:
   config.py:

       #Wireless network

       WiFiSSID =  "<YourSSID>"

       WiFiPassword = "<YourPassword>"

       #MQTT configuration

       mqttserver = "<YourRaspberryPiIP>"

   boot.py:

    import config

    import network

    from time import sleep

    def connect():

        wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
        if not wlan.isconnected():                  # Check if already connected
            print('connecting to network...')
            wlan.active(True)                       # Activate network interface

            # set power mode to get WiFi power-saving off (if needed)
            wlan.config(pm = 0xa11140)
            wlan.connect(config.WiFi_SSID, config.WiFi_Password)  # Your WiFi Credential imported from *config.py*
            print('Waiting for connection...', end='')

            # Check if it is connected otherwise wait
            while not wlan.isconnected() and wlan.status() >= 0:
                print('.', end='')
                sleep(1)
        # Print the IP assigned by router
        ip = wlan.ifconfig()[0]
        print('\nConnected on {}'.format(ip))
        return ip

    def disconnect():

        wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
        wlan.disconnect()
        wlan = None 

main loop of main.py:

    # Change these values based on your water sensor calibration values
        lowerThreshold = 15000
        upperThreshold = 25000
    #Main loop
    
       def mainloop():

        try:
            connect_wifi()
            client = connect_mqtt()

            # Reset RGB LED and Buzzer
            red_led.value(0)
            blue_led.value(0)
            green_led.value(0)
            buzzer.value(0)

            while True:
                client.check_msg()

                water_level = water_sensor_pin.read_u16()
                sensor.measure()
                temp = sensor.temperature()
                hum = sensor.humidity()

                publish_data(client)
                update_oled(temp, hum, water_level)
                control_led_buzzer(water_level)

                formatted_data = format_sensor_data(temp, hum, water_level)
                print(formatted_data)
                print()  # Add an empty line after printing the sensor data

                utime.sleep(1) # Handles the frequency in which the data is sent

        except KeyboardInterrupt:
            pass

        finally:
            try:
                client.disconnect()
                print("Disconnected from MQTT broker")
                oled.fill(0)
                oled.text("MQTT Disconnected", 0, 0)
                oled.show()
            except OSError as e:
                pass

            # Clear the OLED display
            oled.fill(0)
            oled.show()

            # Turn off all LEDs and the buzzer
            red_led.value(0)
            blue_led.value(0)
            green_led.value(0)
            buzzer.value(0) 
    
## Data Transmission and/ Connectivity
As briefly mentioned in the [description](#Description), this project utilizes a Raspberry Pi IoT server for data transmission. The server is set up using MQTT, Node-RED, InfluxDB, and Grafana. 

A brief description about the actual data transmission intervals, protocol and choices made is:

#### 1. Frequency of Data Transmission
The data is sent every 1 second. This is controlled by the *utime.sleep(1)* function call in the main loop of the code. This can be adapted to your own prefenrence and need.

#### 2. Choice of Wireless Protocol
WiFi protocol is utilized. The Raspberry Pi Pico W connects to a WiFi network to transmit data.

#### 3. Transport Protocol used
The MQTT (Message Queuing Telemetry Transport) protocol is used for data transmission in this project. The code utilizes the *umqtt.simple* library to connect to an MQTT broker and publish sensor data.

#### 4. Design Choices for Data Transmission and Wireless Protocols
* Design choice rationale:

    The decision to use WiFi as the wireless protocol in this project is based on its widespread availability and the built-in wireless capability of the Raspberry Pi Pico W.
* Power consumption:
     
     Although WiFi communication generally consumes more power than other wireless protocols like LoRa, the impact on power consumption is negligible due to the indoor nature of this application and its integration into an existing system.
* Security:
    * When using WiFi and MQTT, security considerations are important.
    * To ensure security, it is crucial to secure the WiFi network with a strong password and enable encryption.
    * MQTT can be further secured by implementing authentication and encryption between the device and the MQTT broker.
* Conclusion:
    
    The choice of WiFi and MQTT strikes a balance between ease of implementation, data efficiency, and potential security considerations.
    
#### 5. Data Management
* This project simplifies data and application management by using Docker containers and the Portainer container management tool. 
* Portainer facilitates easy management of Docker containers, including the InfluxDB container used for data storage. 
* The data saving frequency is determined by the code implementation, and in the provided code, data is saved in the InfluxDB database every [1 second](#1-Frequency-of-Data-Transmission). This frequency can be adjusted to meet project-specific requirements.

## Data Presentation
#### 1. Grafana dashboard preview

| State | Preview  |
| ------| -------- |
| All conditions are met   | ![](https://hackmd.io/_uploads/HJIPWqFuh.png)|
| None of the conditions are met    |![](https://hackmd.io/_uploads/rkIc75Y_h.png)    |
|Water level - Normal, Temperature - Low, Humidity - High| ![](https://hackmd.io/_uploads/BkECX5F_n.png)    |
|Water level - Too High, Both Temperature and Humidity - Low    |![](https://hackmd.io/_uploads/Skv545Kdn.png)    |
|Temperature - High, Both Humidity and Water level - Normal    |![](https://hackmd.io/_uploads/rkE1I5tO2.png)    |

#### 2. Choice of Database and Visualization Tool
In this project, I have chosen to integrate Grafana with InfluxDB to address the visualization aspect. This integration allows for the creation of visually compelling representations of sensor data. Here's how Grafana fulfills the visualization requirements of this project:

##### 2.1. Interactive Dashboards:
* Grafana allows the creation of customizable dashboards to display real-time and historical data from InfluxDB.
* Panels and widgets can be arranged on the dashboard to visualize different data aspects like temperature, humidity, and water level.
* A variety of visualization types, such as graphs, gauges, and tables, can be used to present the data.
* Gauges were selected as the visualization type for this project.

##### 2.2. Real-time Monitoring:
Grafana's alerting feature provides timely notifications based on specific data conditions. In this project, Discord webhooks are used for alerts when temperature, humidity, or water measurements exceed tolerance levels. Configurations include:

* Alerts evaluated for five minutes, avoiding premature triggering.
* A one-hour waiting window after each successful alert to prevent alert fatigue.
##### 2.4. Customization and Sharing:
Integrating Grafana with InfluxDB enables powerful data visualization capabilities, enhancing data understanding, decision-making, and communication. It provides an intuitive and customizable way to explore sensor data, fostering effective sharing of insights.

## Final Project Results
Even though this is a prototype project, sensor accuracy played a crucial role in ensuring reliable monitoring of temperature and humidity in the egg incubator. The DHT11 sensor was considered for its affordability and availability. However, upon comparing it with the BME680 sensor, the BME680 proved to offer significantly higher accuracy.

The BME680 sensor has an approximate temperature accuracy of ±0.5°C, while the DHT11 has an accuracy of about ±2°C. Similarly, the BME680 provides humidity accuracy of around ±3% RH, while the DHT11 has an accuracy of about ±5% RH. These comparisons clearly demonstrate the superior accuracy of the BME680 sensor.

Given the critical nature of maintaining precise climate conditions for successful egg incubation, the highly accurate BME680 sensor is recommended. Its accuracy ensures more reliable monitoring and increases the chances of successful incubation and hatching.

It's important to note that periodic calibration and validation of the sensor readings are necessary to maintain ongoing accuracy and reliability in the incubation process.

#### Media
* Images
    * Dry-run
    ![](https://hackmd.io/_uploads/ry1c-TF_3.png)
    ![](https://hackmd.io/_uploads/rkvJM6Kd3.png)

    * Integrated to egg incubator
    ![](https://hackmd.io/_uploads/BJwE4pFdn.png)
    ![](https://hackmd.io/_uploads/BkkJv6Ydh.png)
    ![](https://hackmd.io/_uploads/Sy4jh6Yu3.png)
    
* Videos
    * Water Level Status | Low | High | Normal: https://youtu.be/yArwJZXPQfE
    * Demo: https://youtu.be/K9IM_KOFLCc
