**Description:** 

In this tutorial, you will learn how to build a temperature, humidity, and water level monitoring system using Raspberry Pi Pico W, an HDT11 sensor to measure temperature and humidity, and a water level sensor. 
The system utilizes Docker to log and share sensor data on a Raspberry Pi, with the following components:
* Mosquitto: Message broker for data communication.
* InfluxDB: Database for storing sensor data.
* Node-RED: Data bridge for processing and routing data.
* Grafana: Visualization tool for displaying sensor data.

Additionally, the system incorporates an OLED display, RGB LED, and Buzzer for local visualization and alert notifications.

Time Allocation:

The assembly and coding process for this tutorial can generally be completed within a reasonable timeframe of approximately 1-2 hours. However, it's important to consider personal preferences in terms of data visualization choices and the time needed to become familiar with the components and tools used in the project.

Here's a breakdown of the time allocation for each step:

1. Preparing Raspberry Pi Pico W and connecting the components:
    * This step typically takes around 30 minutes to 1 hour, depending on your familiarity with the hardware and breadboard connections.
2. Writing the code:
    * The provided code is ready to use, but understanding it and making any necessary modifications or customizations may require around 1-2 hours for an average beginner.
3. Setting up the Raspberry Pi to host the required services:
    * This step involves installing and configuring Docker, Portainer, Mosquitto MQTT broker, Node-RED, InfluxDB and Grafana on the Raspberry Pi.
    * On average, an additional 1-2 hours for an average beginner will be required to complete this setup. The actual time required may vary based on your familiarity with the tools and the complexity of the setup.

Please note that these time estimates are approximate and can vary depending on individual experience, learning speed, and familiarity with the tools and concepts involved. It's always recommended to allocate some extra time for troubleshooting and debugging, as unforeseen challenges may arise during the process.

**Objective:**

The objective of this project is to enhance an existing egg incubator by adding a monitoring system that allows remote climate monitoring. Even when away from the incubator, this system enables the user to monitor the climate conditions inside.
In an egg incubator, the hatching process requires specific conditions such as proper egg rotation, correct temperature, and humidity levels. The water level plays a role in influencing humidity. However, as the rotation is handled by the incubator's motor, this monitoring system focuses only on monitoring temperature, humidity, and water level.
To ensure successful hatching, the temperature and humidity need to be maintained within certain tolerance levels during different periods of the incubation process:

| Period                     | Temperature | Humidity |
| -------------------------- | ----------- | -------- |
| First 18 days              | 37.7 °C     | 57%      |
| Last 3 days of the 21 days | 36.9 °C     | 70%      |

By receiving real-time sensor data, the user can take prompt action when necessary. The ability to monitor the climate conditions remotely relieves the burden and limitation of only being able to monitor the incubator when physically present.

**Material:**

*The selection of materials can be tailored according to the user's preferences, and it is recommended to refer to the equipment datasheets for comprehensive specifications and details of the individual components.

| Preview | Item | Description |Approximate price        |
| -------- | -------- | -------- |--------        |
| ![](https://hackmd.io/_uploads/B1Sczwvun.jpg)  | 1 x Raspberry Pi Pico W, with pre-soldered 40-pin header and micro USB-USB-A Cable     | The Raspberry Pi Pico W is a microcontroller board that serves as the central component of this project. It provides the necessary computing power and I/O capabilities to interface with the sensors and other peripherals. The Raspberry Pi Pico W will be responsible for collecting sensor data, executing the monitoring logic, and facilitating the communication with other components of the system.     |138.00 SEK            |
| ![](https://hackmd.io/_uploads/HyWafwP_h.jpg)  | 1 x DHT11 Sensor – Temperature and humidity sensor     | The temperature range of DHT11 is from 0 to 50 degree Celsius with a 2-degree accuracy. Humidity range of this sensor is from 20 to 80% with 5% accuracy. The sampling rate of this sensor is 1Hz .i.e. it gives one reading for every second.  DHT11 is small in size with operating voltage from 3 to 5 volts. The maximum current used while measuring is 2.5mA.3     |78.00 SEK            |
| ![](https://hackmd.io/_uploads/rJ_kQvw_3.jpg)  | 1 x Water level sensor     | Analog signal conversion and output analog values can be directly read by a Micro Controller board to achieve the level alarm effect. It is obtained by having a series of parallel wires exposed tracks measured drops/water volume to determine the water level. Operating temperature: 10 °C - 30 °C, humidity: 10% - 90% non-condensing Operating voltage: DC 3-5V, operating current: less than 20mA, detection area: 40mm x 16mm     |132.00 SEK            |
| ![](https://hackmd.io/_uploads/rysZmPw_3.jpg)  | 1 x OLED Display     | The 0.96" diagonal OLED display used in this tutorial is a compact and vibrant screen comprised of 128x64 individual blue pixels. It provides a clear and concise visual interface to display real-time information such as temperature, humidity, and water level readings. With its small form factor, it can be easily integrated into the monitoring system, offering local visualization of the data in a user-friendly manner.     |77.00 SEK            |
| ![](https://hackmd.io/_uploads/BymEmvvd2.jpg)  | 1 x RGB led     | The KY-009 SMD Module LED RGB 3 Full Color is a versatile component used for colorful visual indicators in the tutorial. This module consists of three RGB (Red, Green, Blue) LEDs in a compact surface-mount device (SMD) package. In the tutorial, the KY-009 module is utilized to provide local visual feedback, indicating various states or conditions of the monitoring system     |116.00 SEK            |
| ![](https://hackmd.io/_uploads/rkFLQwPuh.jpg)  | 1 x Buzzer     | The passive piezo buzzer module is a small audio device that adds an audible alert functionality to the tutorial project. It consists of a piezoelectric element that generates sound when an electrical signal is applied to it. In the tutorial, the module is used to produce sound alerts or notifications based on specific events or conditions. It can be programmed to emit different tones or patterns to indicate different states or warnings within the monitoring system. The piezo buzzer module enhances the user experience by providing an additional sensory feedback element, allowing users to receive auditory cues and respond to the system's status or alerts even without actively monitoring the visual interface.     |68.00 SEK           |
| ![](https://hackmd.io/_uploads/ryytXvw_n.jpg)  | 3 x mini breadboards and 23 X Jumper wires (13pcs male/male 0.64mm pins 100mm,  6pcs female/male and 4pcs 150mm male/male)     | Jumper wires and mini breadboards are versatile connectors used in electronics projects to establish connections between various components. They provide a flexible and convenient way to link different parts of a circuit, enabling easy prototyping and experimentation. With different lengths and colors available, jumper wires offer flexibility in organizing and routing connections within your project. They are an      |111.00 SEK            |


**Preparation**
1. Download and Install Thonny IDE:
    * Visit the Thonny IDE website at https://thonny.org/ and download the appropriate version for your operating system.
    * Follow the installation instructions provided on the website to install Thonny IDE on your computer.
2. Raspberry Pi Pico W Firmware Installation:
    * Download the firmaware for Raspberry Pi Pico W from [fimaware](https://projects.raspberrypi.org/en/projects/get-started-pico-w/1)
    * Locate the downloaded .uf2 firmware file, which is typically stored in the "Downloads" folder. The current version of the firmware at the time of writing this tutorial is *rp2-pico-w-20230426-v1.20.0.uf2*.
    * Connect the Micro USB end of the cable to your Raspberry Pi Pico W prior to connecting it to your computer.
    * Press and hold the BOOTSEL button on your Raspberry Pi Pico W.
    * While holding the BOOTSEL button, connect the USB-A or USB-C end of the cable to your computer.
    * Your file manager should open, and you will see the Raspberry Pi Pico displayed as an externally connected drive.
    * Drag and drop the downloaded .uf2 firmware file into the file manager window.
    * The Raspberry Pi Pico will disconnect, and the file manager window will close.
3. Using Thonny editor:
    * Launch the Thonny editor, which you installed in the previous step.
    * In the bottom right-hand corner of the Thonny editor, you will see some text indicating the currently selected Python version.
    * If it does not display "MicroPython (Raspberry Pi Pico) . COM", click on the text and select "MicroPython (Raspberry Pi Pico)" from the available options.

These steps will prepare your system and Raspberry Pi Pico W for the subsequent stages of the tutorial.

**Hardware connection**
* Component Wiring Instructions for Raspberry Pi Pico W:
    1. Water Level Sensor:
        * Connect the VCC pin of the water level sensor to a 3.3V power source on the Raspberry Pi Pico W. 
        * Connect the GND pin of the water level sensor to a ground (GND) pin on the Raspberry Pi Pico W.
        * Connect the OUT pin of the water level sensor to ADC(2) pin (Pin 28) on the Raspberry Pi Pico W.
    2. DHT11 Sensor:
        * Connect the VCC pin of the DHT11 sensor to a 3.3V power source on the Raspberry Pi Pico W.
        * Connect the GND pin of the DHT11 sensor to a ground (GND) pin on the Raspberry Pi Pico W.
        * Connect the DATA pin of the DHT11 sensor to GP22 pin (Pin 22) on the Raspberry Pi Pico W.
    3. RGB LED:
        * Connect the minus pin of the RGB module to a ground (GND) pin on the Raspberry Pi Pico W.
        * Connect the blue_led pin of the RGB LED module to a GPIO pin on the Raspberry Pi Pico W. (Pin 2)
        * Connect the red_led pin of the RGB LED module to a GPIO pin on the Raspberry Pi Pico W. (Pin 3)
        * Connect the green_led pin of the RGB LED module to a GPIO pin on the Raspberry Pi Pico W. (Pin 4)
        * Make sure to connect each pin of the RGB LED module to the respective GPIO pins on the Raspberry Pi Pico W as indicated above. This will enable control of the individual colors (blue, red, and green) of the RGB LED module through the Raspberry Pi Pico W.
    4. Buzzer:
        * Connect the buzzer pin of the Buzzer module to a GPIO pin on the Raspberry Pi Pico W. (Pin 5)
        * Connect the minus pin of the Buzzer module to a ground (GND) pin on the Raspberry Pi Pico W.
        * Connect the VCC pin of the Buzzer module to a 3.3V power source on the Raspberry Pi Pico W.
    5. OLED Display (I2C Interface):
        * Connect the VCC pin of the OLED display to a 3.3V power source on the Raspberry Pi Pico W.
        * Connect the GND pin of the OLED display to a ground (GND) pin on the Raspberry Pi Pico W.
        * Connect the SDA pin of the OLED display to the SDA pin (Pin 26) on the Raspberry Pi Pico W.
        * Connect the SCL pin of the OLED display to the SCL pin (Pin 27) on the Raspberry Pi Pico W.
By following these wiring instructions, you will establish the necessary electrical connections between the components and the Raspberry Pi Pico W, allowing them to communicate and interact effectively.

* Raspberry Pi Pico W Pinout diagram
![](https://hackmd.io/_uploads/B1nDicD_2.png)

* Assemble the Components:
    * Begin by gathering all the required components for the project.
    * Follow the circuit diagram or specified wiring instructions.
    * Connect the components to the Raspberry Pi Pico W according to the specified pin configurations.
    * Ensure proper connections and secure them in place.
    
By carefully assembling the components, you will create the necessary physical connections between the sensors, modules, and Raspberry Pi Pico W, enabling them to communicate and function together effectively.
    
    Note that actual components may differ from the ones shown in the example, 
    but the general principles of connection remain the same.
![](https://hackmd.io/_uploads/SJACbqPun.png)

**Code and prerequisit for running the code**
* Required libraries 
    1. utime: This library provides functions for working with time and delays.
    2. ubinascii: This library provides functions for working with binary and ASCII data.
    3. ujson: This library provides functions for working with JSON data.
    4. machine: This library provides access to various hardware components and interfaces on the microcontroller.
    5. dht: This library allows you to interact with DHT series temperature and humidity sensors.
    6. network: This library provides network-related functions and classes, such as connecting to Wi-Fi networks.
    7. umqtt.simple: This library provides a simple MQTT client implementation for MicroPython.
    8. ssd1306: This library allows you to communicate with SSD1306-based OLED displays.
    9. boot: This is a custom module specific to your project, so make sure to have the boot.py file available.

* Code snippet

    config.py:

    # Wireless network
    *WiFiSSID =  "<YourSSID>"*

    *WiFiPassword = "<YourPassword>"*

    # MQTT configuration
    *mqttserver = "<YourRaspberryPiIP>"*

    boot.py:

    *import config*

    *import network*

    *from time import sleep*

    '''
    *def connect():*

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

    *def disconnect():*

        wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
        wlan.disconnect()
        wlan = None 
    '''

    main loop for main.py:
    
    # Main loop
   *def mainloop():*

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

                utime.sleep(1)

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
    '''

    **Data transmission/ connectivity**


    **Data presentation**

    **Final project results**
