from machine import Pin, I2C
import time
from pico_i2c_lcd import I2cLcd
import random

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

buzzer = Pin(10, Pin.OUT)
sensor = Pin(11, Pin.IN, Pin.PULL_UP)
greetings = ["Hello!", "How are you\ndoing?", "What's up!", "Hi!",]

buzzer.value(0)

lcd.clear()
lcd.putstr("Starting...")
time.sleep(2)
lcd.clear()
lcd.putstr("Ready!")

while True:
    if sensor.value() == 0:
        current_greeting = random.choice(greetings)
        lcd.clear()
        lcd.putstr(current_greeting)
        buzzer.value(1)
        time.sleep(0.1)
        buzzer.value(0)
        time.sleep(1.9)
        lcd.clear()
        lcd.putstr("Ready...")
    time.sleep(0.05)
    

