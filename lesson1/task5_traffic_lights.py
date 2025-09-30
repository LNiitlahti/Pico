# task5_traffic_lights.py - Traffic lights with buzzer alarm (C) Lassi Niitlahti

# This program simulates traffic lights that cycle through red, yellow, and green
# When the button is pressed, red light turns on and buzzer sounds
# After a delay, the buzzer stops and normal cycling resumes

from machine import Pin, PWM # type: ignore (VSCODE error bypass)
import time

# Set up the traffic light LEDs
red_led = Pin(15, Pin.OUT)
yellow_led = Pin(14, Pin.OUT)
green_led = Pin(13, Pin.OUT)

# Set up the buzzer with PWM for sound
buzzer = PWM(Pin(12))

# Set up the button with pull-down resistor
button = Pin(11, Pin.IN, Pin.PULL_DOWN)

# Function to turn all lights off
def all_lights_off():
    red_led.off()
    yellow_led.off()
    green_led.off()

# Function to sound the buzzer
def buzzer_on():
    buzzer.freq(300)  # Set frequency to 300 Hz
    buzzer.duty_u16(8192)  # 12,5% duty cycle

# Function to turn buzzer off
def buzzer_off():
    buzzer.duty_u16(0)

# Main program loop
print("Traffic lights starting...")

while True:
    # Check if button is pressed
    if button.value() == 1:
        # Emergency mode: Red light and buzzer
        all_lights_off()
        red_led.on()
        buzzer_on()
        print("Emergency! Button pressed!")
        
        # Wait while button is held and for 3 seconds after
        time.sleep(3)
        
        # Turn off buzzer but keep red light on briefly
        buzzer_off()
        time.sleep(1)
        
        print("Resuming normal operation...")
    
    # Normal traffic light cycle
    # Green light
    all_lights_off()
    green_led.on()
    print("Green light")
    time.sleep(3)
    
    # Check for button during green
    if button.value() == 1:
        continue
    
    # Yellow light
    all_lights_off()
    yellow_led.on()
    print("Yellow light")
    time.sleep(1)
    
    # Check for button during yellow
    if button.value() == 1:
        continue
    
    # Red light
    all_lights_off()
    red_led.on()
    print("Red light")
    time.sleep(3)
    
    # Small delay to avoid button bounce
    time.sleep(0.01)