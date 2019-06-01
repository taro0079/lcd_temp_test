import lcddriver
import time
import RPi.GPIO as GPIO
import time
import datetime
import dht11

display = lcddriver.lcd()
display.lcd_clear()

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

instance = dht11.DHT11(pin=17) # select pin

try:
    while True:
        result = instance.read()
        if result.is_valid():
            display.lcd_display_string("Temperature:" + str(result.temperature),1) # write temperature in first line of LCD
            display.lcd_display_string("Humidity:" + str(result.humidity), 2) # write humidity in second line of LCD

except KeyboardInterrupt:
    display.lcd_clear()
