# task7_burglary_alarm.py - Burglary alarm with PIR sensor (C) Lassi Niitlahti

# This program monitors a PIR (Passive Infrared) motion sensor
# When motion is detected, it triggers an alarm with LED and buzzer
# The alarm stays active for a set time period

from machine import Pin, PWM # type: ignore (VSCODE error bypass)
import time

# Set up PIR sensor on GP15 as input
pir_sensor = Pin(15, Pin.IN)

# Set up LED on GP14 as output (alarm indicator)
alarm_led = Pin(14, Pin.OUT)

# Set up buzzer with PWM on GP13 for alarm sound
buzzer = PWM(Pin(13))

# Variable to track alarm state
alarm_active = False

# Function to sound the alarm
def sound_alarm():
    buzzer.freq(800)  # Set frequency to 800 Hz for alarm sound
    buzzer.duty_u16(16384)  # 25% duty cycle for buzzer

# Function to turn alarm off
def alarm_off():
    buzzer.duty_u16(0)  # Turn off buzzer
    alarm_led.off()  # Turn off LED

# Function to activate alarm sequence
def activate_alarm():
    print("ALARM! Motion detected!")
    alarm_led.on()  # Turn on alarm LED
    sound_alarm()  # Start buzzer
    
    # Keep alarm active for 5 seconds
    time.sleep(5)
    
    # Turn off alarm
    alarm_off()
    print("Alarm stopped. Monitoring...")

# Main program
print("===== BURGLARY ALARM SYSTEM =====")
print("System armed and monitoring...")
print("Waiting for motion detection...")
print()

# Main monitoring loop
while True:
    # Check if PIR sensor detects motion
    if pir_sensor.value() == 1:
        # Motion detected - activate alarm
        activate_alarm()
        
        # Wait a bit before monitoring again to avoid repeated triggers
        time.sleep(2)
    
    # Small delay to avoid excessive checking
    time.sleep(0.1)