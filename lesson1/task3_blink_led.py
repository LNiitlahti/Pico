# task3_blink_led.py - Blink external LED on GP15 (C) Lassi Niitlahti

# This program blinks an external LED connected to GPIO pin 15
# The LED turns on for 1 second, then off for 1 second, repeatedly

from machine import Pin # type: ignore (VSCODE error bypass)
import time

# Set up the external LED connected to GP15
led = Pin(15, Pin.OUT)

# Main loop - runs forever
while True:
    led.on()           # Turn the LED on
    time.sleep(1)      # Wait for 1 second
    led.off()          # Turn the LED off
    time.sleep(1)      # Wait for 1 second