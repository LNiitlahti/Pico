# task4_button_led.py - Button controlled LED (C) Lassi Niitlahti

# This program turns an LED on when a button is pressed
# LED stays on while button is held down
# LED turns off when button is released

from machine import Pin # type: ignore (VSCODE error bypass)
import time

# Set up the LED on GP15 as output
led = Pin(15, Pin.OUT)

# Set up the button on GP14 as input with pull-down resistor
# Pull-down means the pin reads 0 when button is not pressed
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Main loop - runs forever
while True:
    if button.value() == 1:    # If button is pressed
        led.on()               # Turn LED on
    else:                      # If button is not pressed
        led.off()              # Turn LED off
    
    time.sleep(0.01)           # Small delay to avoid excessive checking