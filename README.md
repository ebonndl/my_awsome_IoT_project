By Bongani Ndlovu, (bn222if)
# Table of Contents
[TOC]
## Description

In this tutorial, you will learn how to build a temperature, humidity, and water level monitoring system using [Raspberry Pi Pico W](https://www.electrokit.com/produkt/raspberry-pi-pico-w/?gclid=EAIaIQobChMItKbR_tzl_wIVcuTmCh3C4A1tEAAYAiAAEgIIqPD_BwE), a DHT11 sensor will measure temperature and humidity, a water level sensor will be used to monitor the amount of water. 
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

## Objective

The objective of this project is to enhance an existing egg incubator by adding a monitoring system that allows remote climate monitoring. Even when away from the incubator, this system enables the user to monitor the climate conditions inside.
In an egg incubator, the hatching process requires specific conditions such as proper egg rotation, correct temperature, and humidity levels. The water level plays a role in influencing humidity. However, as the rotation is handled by the incubator's motor, this monitoring system focuses only on monitoring temperature, humidity, and water level.
To ensure successful hatching, the temperature and humidity need to be maintained within certain tolerance levels during different periods of the incubation process:

| Period                     | Temperature | Humidity |
| -------------------------- | ----------- | -------- |
| First 18 days              | 37.7 °C     | 57%      |
| Last 3 days of the 21 days | 36.9 °C     | 70%      |

By receiving real-time sensor data, the user can take prompt action when necessary. The ability to monitor the climate conditions remotely relieves the burden and limitation of only being able to monitor the incubator when physically present.

## Material

The selection of materials can be tailored according to the user's preferences, and it is recommended to refer to the equipment datasheets for comprehensive specifications and details of the individual components.

| Preview                                       | Item                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Approximate price |     |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --- |
| ![](https://hackmd.io/_uploads/B1Sczwvun.jpg) | 1 x [Raspberry Pi Pico W](https://www.electrokit.com/produkt/raspberry-pi-pico-w/?gclid=EAIaIQobChMItKbR_tzl_wIVcuTmCh3C4A1tEAAYAiAAEgIIqPD_BwE), with pre-soldered 40-pin header and micro USB-USB-A Cable                                                                                                                                               | The Raspberry Pi Pico W is a microcontroller board that serves as the central component of this project. It provides the necessary computing power and I/O capabilities to interface with the sensors and other peripherals. The Raspberry Pi Pico W will be responsible for collecting sensor data, executing the monitoring logic, and facilitating the communication with other components of the system.                                                                                                                                                                                                                                                                                                                                 | 138.00 SEK        | 
| ![](https://hackmd.io/_uploads/HyWafwP_h.jpg) | 1 x [DHT11 Sensor](https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/) – Temperature and humidity sensor                                                                                                                                                                                                                         | The temperature range of DHT11 is from 0 to 50 degree Celsius with a 2-degree accuracy. Humidity range of this sensor is from 20 to 80% with 5% accuracy. The sampling rate of this sensor is 1Hz .i.e. it gives one reading for every second.  DHT11 is small in size with operating voltage from 3 to 5 volts. The maximum current used while measuring is 2.5mA.3                                                                                                                                                                                                                                                                                                                                                                         | 78.00 SEK         |
| ![](https://hackmd.io/_uploads/rJ_kQvw_3.jpg) | 1 x [Water level sensor](https://www.fruugo.se/5-pieces-rain-water-sensor-liquid-level-sensor-rain-water-detection-for-detection-area-40mmx16mm/p-119987351-252224651?language=en&ac=ProductCasterAPI&asc=pmax&gclid=EAIaIQobChMIm9uHyN_l_wIV2fhRCh2aAwAUEAQYDCABEgJ_oPD_BwE)                                                                             | Analog signal conversion and output analog values can be directly read by a Micro Controller board to achieve the level alarm effect. It is obtained by having a series of parallel wires exposed tracks measured drops/water volume to determine the water level. Operating temperature: 10 °C - 30 °C, humidity: 10% - 90% non-condensing Operating voltage: DC 3-5V, operating current: less than 20mA, detection area: 40mm x 16mm                                                                                                                                                                                                                                                                                                       | 132.00 SEK (5pcs) |
| ![](https://hackmd.io/_uploads/rysZmPw_3.jpg) | 1 x [OLED Display](https://www.amazon.se/AZDelivery-I2C-Skärm-kompatibel-Raspberry-inklusive/dp/B01L9GC470/ref=asc_df_B01L9GC470/?tag=shpngadsglede-21&linkCode=df0&hvadid=476458655005&hvpos=&hvnetw=g&hvrand=2169706603414924&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012324&hvtargid=pla-402608082122&psc=1)                      | The 0.96" diagonal OLED display used in this tutorial is a compact and vibrant screen comprised of 128x64 individual blue pixels. It provides a clear and concise visual interface to display real-time information such as temperature, humidity, and water level readings. With its small form factor, it can be easily integrated into the monitoring system, offering local visualization of the data in a user-friendly manner.                                                                                                                                                                                                                                                                                                         | 77.00 SEK         |
| ![](https://hackmd.io/_uploads/BymEmvvd2.jpg) | 1 x [RGB LED SMD](https://www.electrokit.com/produkt/led-modul-rgb-smd/)                                                                                                                                                                                                                                                                          | The KY-009 SMD Module LED RGB 3 Full Color is a versatile component used for colorful visual indicators in the tutorial. This module consists of three RGB (Red, Green, Blue) LEDs in a compact surface-mount device (SMD) package. In the tutorial, the KY-009 module is utilized to provide local visual feedback, indicating various states or conditions of the monitoring system                                                                                                                                                                                                                                                                                                                                                        | 116.00 SEK        |
| ![](https://hackmd.io/_uploads/rkFLQwPuh.jpg) | 1 x [Buzzer](https://www.electrokit.com/produkt/piezohogtalare-passiv/)                                                                                                                                                                                                                                                                                   | The passive piezo buzzer module is a small audio device that adds an audible alert functionality to the tutorial project. It consists of a piezoelectric element that generates sound when an electrical signal is applied to it. In the tutorial, the module is used to produce sound alerts or notifications based on specific events or conditions. It can be programmed to emit different tones or patterns to indicate different states or warnings within the monitoring system. The piezo buzzer module enhances the user experience by providing an additional sensory feedback element, allowing users to receive auditory cues and respond to the system's status or alerts even without actively monitoring the visual interface. | 68.00 SEK         |
| ![](https://hackmd.io/_uploads/ryytXvw_n.jpg) | 3 x [mini breadboards](https://www.amazon.se/AZDelivery-Breadboard-Kit-Bygelkabel-kompatibel/dp/B07NJ3FX25/ref=sr_1_4?crid=34VBKF5QMOFDY&keywords=3%2Bx%2Bmini%2Bbreadbord&qid=1687948256&sprefix=3%2Bx%2Bmini%2Bbreadbord%2Caps%2C220&sr=8-4&th=1) and 23 X Jumper wires (13pcs male/male 0.64mm pins 100mm,  6pcs female/male and 4pcs 150mm male/male) | Jumper wires and mini breadboards are versatile connectors used in electronics projects to establish connections between various components. They provide a flexible and convenient way to link different parts of a circuit, enabling easy prototyping and experimentation. With different lengths and colors available, jumper wires offer flexibility in organizing and routing connections within your project. They are an                                                                                                                                                                                                                                                                                                              | 111.00 SEK        |
|                                               |                                                                                                                                                                                                                                                                                                                                                           | Total:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 714.00 SEK                   |

## Preparation
#### 1. Download and Install Thonny IDE:
* Visit the Thonny IDE website at https://thonny.org/ and download the appropriate version for your operating system.
* Follow the installation instructions provided on the website to install Thonny IDE on your computer.
#### 2. Raspberry Pi Pico W Firmware Installation:
* Download the firmaware for Raspberry Pi Pico W from [fimaware](https://projects.raspberrypi.org/en/projects/get-started-pico-w/1)
* Locate the downloaded .uf2 firmware file, which is typically stored in the "Downloads" folder. The current version of the firmware at the time of writing this tutorial is *rp2-pico-w-20230426-v1.20.0.uf2*.
* Connect the Micro USB end of the cable to your Raspberry Pi Pico W prior to connecting it to your computer.
* Press and hold the BOOTSEL button on your Raspberry Pi Pico W.
* While holding the BOOTSEL button, connect the USB-A or USB-C end of the cable to your computer.
* Your file manager should open, and you will see the Raspberry Pi Pico displayed as an externally connected drive.
* Drag and drop the downloaded .uf2 firmware file into the file manager window.
* The Raspberry Pi Pico will disconnect, and the file manager window will close.
#### 3. Using Thonny Editor:
* Launch the Thonny editor, which you installed in the previous step.
* In the bottom right-hand corner of the Thonny editor, you will see some text indicating the currently selected Python version.
* If it does not display "MicroPython (Raspberry Pi Pico)" and COM port, click on the text and select "MicroPython (Raspberry Pi Pico)" from the available options. ![Image 1](https://hackmd.io/_uploads/r1n4LOuu2.png)

#### 4. Installing Libraries using Thonny Editor:
   * Launch the Thonny editor, which you installed in the previous step.
   * Ensure that "MicroPython (Raspberry Pi Pico)" is selected at the bottom right-hand corner of the Thonny editor. 
    * Navigate to the Thonny Tools Menu (#*1.*) > Manage packages...(#*2.*)
     ![Image 2](https://hackmd.io/_uploads/HyR7KO_u3.png)
   * In the popup menu, type the name of the library you want to install into the search field (#*3.*) and Click Search on PyPI (#*4.*).
    
   ![Image 3](https://hackmd.io/_uploads/rkv1nO_d3.png)
   * Select the appropriate library from the search results.
   * Click the Install button (#*5.*) at the bottom of the menu to begin the installation process.
   * Wait for the installation to complete. You will see a progress bar indicating the installation progress.
   * Once the installation is finished, you will be prompted to close the package manager. 
   * Click the Close button (#*6.*) to exit the package manager.

These steps will prepare your system and Raspberry Pi Pico W for the subsequent stages of the tutorial.

## Hardware connection
#### 1. Component Wiring Instructions for Raspberry Pi Pico W:
1.1. Water Level Sensor:
* Connect the VCC pin of the water level sensor to a 3.3V power source on the Raspberry Pi Pico W. 
* Connect the GND pin of the water level sensor to a ground (GND) pin on the Raspberry Pi Pico W.
* Connect the OUT pin of the water level sensor to ADC(2) pin (Pin 28) on the Raspberry Pi Pico W.
    
1.2. DHT11 Sensor:
* Connect the VCC pin of the DHT11 sensor to a 3.3V power source on the Raspberry Pi Pico W.
* Connect the GND pin of the DHT11 sensor to a ground (GND) pin on the Raspberry Pi Pico W.
* Connect the DATA pin of the DHT11 sensor to GP22 pin (Pin 22) on the Raspberry Pi Pico W.
    
1.3. RGB LED:
* Connect the minus pin of the RGB module to a ground (GND) pin on the Raspberry Pi Pico W.
* Connect the blue_led pin of the RGB LED module to a GPIO pin on the Raspberry Pi Pico W. (Pin 2)
* Connect the red_led pin of the RGB LED module to a GPIO pin on the Raspberry Pi Pico W. (Pin 3)
* Connect the green_led pin of the RGB LED module to a GPIO pin on the Raspberry Pi Pico W. (Pin 4)

Make sure to connect each pin of the RGB LED module to the respective GPIO pins on the Raspberry Pi Pico W as indicated above. This will enable control of the individual colors (blue, red, and green) of the RGB LED module through the Raspberry Pi Pico W.

1.4. Buzzer:
* Connect the VCC pin of the Buzzer module to a 3.3V power source on the Raspberry Pi Pico W.
* Connect the minus pin of the Buzzer module to a ground (GND) pin on the Raspberry Pi Pico W.
* Connect the buzzer pin of the Buzzer module to a GPIO pin on the Raspberry Pi Pico W. (Pin 5)

1.5. OLED Display (I2C Interface):
* Connect the VCC pin of the OLED display to a 3.3V power source on the Raspberry Pi Pico W.
* Connect the GND pin of the OLED display to a ground (GND) pin on the Raspberry Pi Pico W.
* Connect the SDA pin of the OLED display to the SDA pin (Pin 26) on the Raspberry Pi Pico W.
* Connect the SCL pin of the OLED display to the SCL pin (Pin 27) on the Raspberry Pi Pico W.

By following these wiring instructions, you will establish the necessary electrical connections between the components and the Raspberry Pi Pico W, allowing them to communicate and interact effectively.

#### 2. Raspberry Pi Pico W Pinout diagram
![](https://hackmd.io/_uploads/B1nDicD_2.png)

#### 3. Assemble the Components:
* Begin by gathering all the required components for the project.
* Follow the circuit diagram or specified wiring instructions.
* Connect the components to the Raspberry Pi Pico W according to the specified pin configurations.
* Ensure proper connections and secure them in place.
    
    By carefully assembling the components, you will create the necessary physical connections between the sensors, modules, and Raspberry Pi Pico W, enabling them to communicate and function together effectively.
    
    Note that actual components may differ from the ones shown in the example, 
    but the general principles of connection remain the same.
![](https://hackmd.io/_uploads/SJACbqPun.png)

## Code and Prerequisites for Running the code

To run the code for this project, you will need the following prerequisites:

#### 1. MicroPython Firmware:
Ensure that you have flashed the MicroPython firmware onto your Raspberry Pi Pico W, as described in the ["Preparation"](#Preparation) section of this tutorial.

#### 2. Required Libraries: 
Install the necessary libraries to your Raspberry Pi Pico W by following the steps provided in the ["Installing Libraries using Thonny Editor"](####4.-Installing-Libraries-using-Thonny-Editor:) section of this tutorial.
  * The following two libraries needs to be installed by follow the above mentioned section;
    1. umqtt.simple: This library provides a simple MQTT client implementation for MicroPython.
    2. ssd1306: This library allows you to communicate with SSD1306-based OLED displays.
* In addition to the above libraries (i.e. *umqtt.simple* and *ssd1306*), the following libraries are part of the MicroPython standard library and should already be available on your Raspberry Pi Pico W. You can directly import them into your project:
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
   * Connect your Raspberry Pi Pico W to your computer using a Micro USB cable.
* Launch the Thonny editor, which you installed during the preparation process.
* Make sure "MicroPython (Raspberry Pi Pico)" is selected as the Python version and the correct COM port is selected in the bottom right-hand corner of the Thonny editor.
* Open the main code file (e.g., main.py) from the extracted code folder in Thonny.
* Click the "Run" button or press F5 to upload and run the code on your Raspberry Pi Pico W.

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
As briefly mentioned in the [description](#Description), this project utilizes a Raspberry Pi IoT server for data transmission. The server is set up using MQTT, Node-RED, InfluxDB, and Grafana. If you want to learn how to set up your own Raspberry Pi IoT server with these services, you can follow this link: https://learnembeddedsystems.co.uk/easy-raspberry-pi-iot-server. The provided guide includes a comprehensive video tutorial that offers step-by-step instructions to help you set up the server and establish data connectivity.

A brief description about the actual data transmission intervals, protocol and choices made is:

#### 1. Frequency of Data Transmission
The data is sent every 1 second. This is controlled by the *utime.sleep(1)* function call in the main loop of the code. This can be adapted to your own prefenrence and need.

#### 2. Choice of Wireless Protocol
This project uses the WiFi protocol for wireless communication. The Raspberry Pi Pico W connects to a WiFi network to transmit the data.

#### 3. Transport Protocol used
The MQTT (Message Queuing Telemetry Transport) protocol is used for data transmission in this project. The code utilizes the *umqtt.simple* library to connect to an MQTT broker and publish sensor data.

#### 4. Design Choices Regarding Data Transmission and Wireless Protocols
* Design choice driver:
    * The choice of using WiFi was driven by the fact that the system used indoor and is incorporated in an existing egg incubator. 
    * This implied that power source was out of the question and the Pico W has Wifi capability.
* Power consumption:
    * It is known fact that WiFi communication can consume more power compared to other wireless protocols like LoRa. However, the impact on battery life can be managed by optimizing the code and minimizing the time the device spends actively transmitting or receiving data. 
    * For example, in the provided code, the data is sent every 1 second, allowing the device to go into low-power mode (*utime.sleep(1)*) between data transmissions.
* Security:
    * Using WiFi and MQTT introduces some security considerations. 
    * It is therefore crucial to secure the WiFi network with a strong password and an encryption of some kind. 
    * MQTT can be secured by enabling authentication and encryption between the device and the MQTT broker. 
    * This ensures that only authorized devices can connect to the MQTT broker and that the data transmitted is encrypted, protecting it from unauthorized access.
* Conclusion:
    * Overall, the choice of WiFi and MQTT strikes a balance between ease of implementation, data efficiency, and potential security considerations.
    * However, depending on the specific project requirements, other wireless protocols like LoRa or transport protocols like webhooks may be more suitable.
    
#### 5. Data Management
* To simplify the management of data and containerized applications, this project utilizes Docker containers and the Portainer container management tool. 
* Portainer enables easy management of Docker containers, including the InfluxDB container used for data storage. 
* The frequency of data saving is determined by the code implementation and in the provided code; data is saved in the InfluxDB database every [1 second](####1._Frequency_of_Data_Transmission). - This can be adjusted according to the specific requirements of the project.

## Data Presentation
#### Grafana dashboard preview

| State                    | Preview              |
| --------                 | --------             |
| All conditions are met   | ![](https://hackmd.io/_uploads/HJIPWqFuh.png)|
| None of the conditions are met    |![](https://hackmd.io/_uploads/rkIc75Y_h.png)    |
|Water level - Normal, Temperature - Low, Humidity - High| ![](https://hackmd.io/_uploads/BkECX5F_n.png)    |
|Water level - Too High, Both Temperature and Humidity - Low    |![](https://hackmd.io/_uploads/Skv545Kdn.png)    |
|Temperature - High, Both Humidity and Water level - Normal    |![](https://hackmd.io/_uploads/rkE1I5tO2.png)    |

#### Choice of Database and Visualization Tool
In this project, I have chosen to integrate Grafana with InfluxDB to address the visualization aspect. This integration allows for the creation of visually compelling representations of sensor data. Here's how Grafana fulfills the visualization requirements of this project:

##### 1. Interactive Dashboards:
* Grafana enables the design of customizable dashboards that showcase real-time and historical data from the InfluxDB database.
* Panels and widgets can be arranged on the dashboard to visualize different aspects of the data, such as temperature, humidity, and water level readings.
* Various visualization types, including graphs, gauges, and tables, can be applied to the panels, providing flexibility in presenting the data. 
* For this project, gauges were chosen as the visualization type.

##### 2. Real-time Monitoring:
* With Grafana, it is possible to monitor the latest sensor readings in real time as they are updated in the InfluxDB database.
* Auto-refresh intervals can be set on the dashboards to ensure the display of the most recent data, facilitating continuous monitoring of changes and prompt responses to critical events.

##### 3. Alerts and Notifications:
* Grafana offers the capability to set up alerts based on specific conditions or thresholds in the data.
* Rules can be defined to trigger notifications, such as emails, SMS messages, or other types of notifications, when certain criteria are met.
* While no alerts have been implemented in this project, the option to set them up is available for proactive monitoring and timely actions when necessary.

##### 4. Customization and Sharing:
* Grafana provides extensive customization options, allowing for personalized appearances of the dashboards and visualizations.
* Colors, fonts, and layouts can be customized to suit individual preferences or meet specific branding requirements.
* Additionally, Grafana facilitates easy sharing and collaboration, enabling the sharing of dashboards with others or embedding them in other applications or websites.

By integrating Grafana with InfluxDB, the project achieves powerful data visualization capabilities, enabling the exploration of sensor data in an intuitive and customizable manner. This enhances the understanding of the data, facilitates informed decision-making, and supports effective communication and sharing of insights.

## Final Project Results
Based on the relationship between the amount of water, temperature, and humidity discussed earlier, it is important to consider the accuracy of the DHT11 sensor in the context of temperature-sensitive environments.

The DHT11 sensor has a temperature accuracy of approximately 2 degrees. While it can provide useful temperature measurements in many applications, it may not be the best choice for environments where temperature accuracy is critical. In such cases, where precise temperature control or monitoring is required, it is recommended to use sensors with higher accuracy specifications.

For applications like egg incubation, where maintaining specific temperature ranges is crucial for successful hatching, using sensors with higher accuracy, such as thermocouples or platinum resistance thermometers (RTDs), may be more appropriate. These sensors offer greater precision and reliability in temperature measurement, ensuring more accurate control and monitoring of the incubation process.

Therefore, when considering the choice of temperature sensors for temperature-sensitive environments, it is important to carefully evaluate the accuracy requirements of the specific application and select sensors accordingly.

#### Media
* Images
    * Dry-run
    ![](https://hackmd.io/_uploads/ry1c-TF_3.png)
    ![](https://hackmd.io/_uploads/rkvJM6Kd3.png)

    * Integrated to egg incubator
    ![](https://hackmd.io/_uploads/BJwE4pFdn.png)
    ![](https://hackmd.io/_uploads/BkkJv6Ydh.png)
    ![](https://hackmd.io/_uploads/Sy4jh6Yu3.png)
    
* Video
    * Water level normal: https://youtu.be/TSoYaD--FXg
    * Water level low: https://youtu.be/-Sz1NxKUpZc
    * Water level high: https://youtu.be/JwAzvJ2NEH0
