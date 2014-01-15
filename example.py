#!/usr/bin/python
# MCP23017 Demonstration
# version 1.0
# Hacklab North Boynton

import RPi.GPIO as GPIO
from Adafruit_MCP230xx import Adafruit_MCP230XX

ENABLE = 1
INPUT = 1
OUTPUT = 0
i2c_device = Adafruit_MCP230XX(address=0x20, num_gpios=16)

def main():
    try:
        while True:
            if (i2c_device.input(0) == 0):
                i2c_device.output(1, 0)
            else:
                i2c_device.output(1, 1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(1)

def setup():
    i2c_device.pullup(0, ENABLE)
    i2c_device.config(1, OUTPUT)
    i2c_device.output(1, 1)

if __name__ == '__main__':
    setup()
    main()
