# MCP23017 Demonstration
# version 1.0
# Hacklab North Boynton

import RPi.GPIO as GPIO
from Adafruit_MCP230xx import Adafruit_MCP230XX

ENABLE = 1
i2c_device = Adafruit_MCP230XX(address=0x20, num_gpios=16)

def main():
    try:
        while True:
            if (i2c_device.input(0) == 0):
                announce_pin(0)

    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(1)

def setup():
    for x in range(0,2):
        i2c_device.pullup(x, ENABLE)

def announce_pin(pin_number):
    print("Pin % is low")

if __name__ == '__main__':
    setup()
    main()
