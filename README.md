**Author: **
Bongani Ndlovu, (bn222if)

**Description:** 
In this tutorial, you will learn how to build a temperature, humidity, and water level monitoring system using Raspberry Pi Pico W, an HDT11 sensor for temperature measurement, and a water level sensor. 
The system utilizes Docker to log and share sensor data on a Raspberry Pi, with the following components:
•	Mosquitto: A message broker for data communication.
•	InfluxDB: A database for storing sensor data.
•	Node-RED: A data bridge for processing and routing data.
•	Grafana: A visualization tool for displaying sensor data.

Additionally, the system incorporates an OLED display, RGB LED, and Buzzer for local visualization and alert notifications.
Apart from data visualization, the assembly and coding process can be completed in approximately one hour, allowing for personal preferences in data visualization choices.

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

