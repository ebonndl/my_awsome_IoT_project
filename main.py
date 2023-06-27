# refactored version of code for egg incubator monitoring system
import utime
import ubinascii
import ujson
import machine
import dht
import network
from umqtt.simple import MQTTClient
import ssd1306
from config import mqtt_server
import boot

# MQTT configuration
mqtt_topic = "sensor_data"

# Initialize Water level sensor on ADC(2)
water_sensor_pin = machine.ADC(machine.Pin(28))

# Initialize DHT11 sensor on GP22
sensor = dht.DHT11(machine.Pin(22))

# Initialize RGB LED pins
blue_led = machine.Pin(2, machine.Pin.OUT)
red_led = machine.Pin(3, machine.Pin.OUT)
green_led = machine.Pin(4, machine.Pin.OUT)

# Initialize Buzzer pin
buzzer = machine.Pin(5, machine.Pin.OUT)

# Initialize I2C interface and OLED display
i2c = machine.I2C(1, scl=machine.Pin(27), sda=machine.Pin(26))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Generate a unique client ID
client_id = ubinascii.hexlify(machine.unique_id()).decode()

# Connect to WiFi
def connect_wifi():
    try:
        ip = boot.connect()
        oled.fill(0)
        oled.text("Connected to WiFi", 0, 0)
        oled.text("IP: {}".format(ip), 0, 16)
        oled.show()
    except KeyboardInterrupt:
        print("Keyboard interrupt")

# Connect to MQTT broker
def connect_mqtt():
    while True:
        try:
            client = MQTTClient(client_id, mqtt_server)
            client.connect(clean_session=False)
            print("Connected to MQTT broker")
            oled.fill(0)
            oled.text("MQTT Connected", 0, 32)
            oled.show()
            return client
        except OSError as e:
            print("Failed to connect to MQTT broker. Retrying...")
            utime.sleep(1)

# Publish sensor data to MQTT broker
def publish_data(client):
    water_level = water_sensor_pin.read_u16()
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()

    data = {
        "temperature": temp,
        "humidity": hum,
        "water_level": water_level
    }

    payload = ujson.dumps(data)
    client.publish(mqtt_topic, payload)

# Update OLED display with sensor data
def update_oled(temp, hum, water_level):
    oled.fill(0)
    oled.text("Sensor Data", 0, 0)
    oled.text("Water Level: {}".format(str(water_level)), 0, 16)
    oled.text("Temp: {}C".format(str(temp)), 0, 32)
    oled.text("Hum: {}%".format(str(hum)), 0, 48)
    oled.show()

# Control RGB LED based on water level
def control_led_buzzer(water_level):
    if water_level == 0 or water_level <= lowerThreshold:
        red_led.value(1)
        blue_led.value(0)
        green_led.value(0)
        buzzer.value(1)
        # Sound the buzzer for 1 second
        buzzer.on()
        utime.sleep(1)
        buzzer.off()
    elif water_level > lowerThreshold and water_level <= upperThreshold:
        red_led.value(0)
        blue_led.value(0)
        green_led.value(1)
        buzzer.off()
    elif water_level > upperThreshold:
        red_led.value(0)
        green_led.value(0)
        blue_led.value(1)
        # Flash the blue LED and sound the buzzer
        for _ in range(5):
            blue_led.toggle()
            buzzer.on()
            utime.sleep(0.5)
            blue_led.toggle()
            buzzer.off()
            utime.sleep(0.5)

# Format sensor data
def format_sensor_data(temp, hum, water_level):
    if water_level == 0 or water_level <= lowerThreshold:
        water_level_status = "Low/Empty"
    elif water_level > lowerThreshold and water_level <= upperThreshold:
        water_level_status = "Normal"
    else:
        water_level_status = "High"

    formatted_data = "Sensor Data\n"
    formatted_data += "Temperature: {}°C\n".format(temp)
    formatted_data += "Humidity: {}%\n".format(hum)
    formatted_data += "Water Level: {} ({})\n".format(water_level, water_level_status)

    return formatted_data

# Change these values based on your water sensor calibration values
lowerThreshold = 15000
upperThreshold = 25000

# Main loop
def main_loop():
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

if __name__ == "__main__":
    main_loop()


