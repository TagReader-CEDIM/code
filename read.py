# Write your code here :-)
#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import strftime
import Adafruit_DHT
import time
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
reader = SimpleMFRC522()
try:
    while True:
        id, text = reader.read()
        print(id)
        print(text)
        dateTime = strftime("%d/%m/%y at %I:%M%p")
        print(dateTime)
        humidity,temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}C Humidity={1:0.1f}".format(temperature,humidity))
        else:
            print("Failed to retrive data from temperature sensor");
finally:
    GPIO.cleanup()
