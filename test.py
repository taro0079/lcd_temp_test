import lcddriver
import time
import RPi.GPIO as GPIO
import time
import datetime


display = lcddriver.lcd()
display.lcd_clear()

# initialize GPIO
GPIO.setwarnings(False)


