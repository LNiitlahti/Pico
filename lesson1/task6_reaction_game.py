# task6_reaction_game.py - Multi-LED reaction time game (C) Lassi Niitlahti

# This program is a fast-paced reaction game with 4 LEDs and 4 buttons
# Press the button that matches the lit LED as fast as you can
# Game gets faster with each correct press
# All LEDs blink if you press the wrong button

from machine import Pin # type: ignore (VSCODE error bypass)
import time
import random

# Set up 4 LEDs on GP15, GP14, GP13, GP12
led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)

# Store LEDs in a list for easy access
leds = [led1, led2, led3, led4]

# Set up 4 buttons on GP11, GP10, GP9, GP8 with pull-down resistors
btn1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
btn2 = Pin(10, Pin.IN, Pin.PULL_DOWN)
btn3 = Pin(9, Pin.IN, Pin.PULL_DOWN)
btn4 = Pin(8, Pin.IN, Pin.PULL_DOWN)

# Store buttons in a list for easy access
buttons = [btn1, btn2, btn3, btn4]

# Game variables
score = 0
delay_time = 1.0  # Starting delay in seconds

# Function to clear the screen
def clear_screen():
    print('\033[2J\033[H')

# Function to turn all LEDs off
def all_leds_off():
    for led in leds:
        led.off()

# Function to turn all LEDs on
def all_leds_on():
    for led in leds:
        led.on()

# Function to make all LEDs blink (wrong answer)
def blink_all_leds():
    for i in range(5):
        all_leds_on()
        time.sleep(0.1)
        all_leds_off()
        time.sleep(0.1)

# Function to check which button is pressed
def check_button_press():
    for i in range(len(buttons)):
        if buttons[i].value() == 1:
            return i
    return -1  # No button pressed

# Function to wait for any button press
def wait_for_button():
    while check_button_press() == -1:
        time.sleep(0.01)
    return check_button_press()

# Function to play one round
def play_round():
    global score, delay_time
    
    # Clear screen for clean display
    clear_screen()
    
    # Display current score
    print("===== REACTION GAME =====")
    print(f"Score: {score}")
    print(f"Speed: {delay_time:.2f}s")
    print("=" * 25)
    
    # Turn off all LEDs first
    all_leds_off()
    time.sleep(0.3)
    
    # Choose random LED to light up
    target_led = random.randint(0, 3)
    
    # Light up the target LED
    leds[target_led].on()
    print(f"\nLED {target_led + 1} is ON! Press button {target_led + 1}!")
    
    # Record start time
    start_time = time.ticks_ms()
    
    # Wait for button press
    pressed_button = wait_for_button()
    
    # Calculate reaction time
    reaction_time = time.ticks_diff(time.ticks_ms(), start_time)
    
    # Check if correct button was pressed
    if pressed_button == target_led:
        # Correct!
        score += 1
        clear_screen()
        print("===== REACTION GAME =====")
        print(f"Score: {score}")
        print("=" * 25)
        print(f"\n✓ CORRECT!")
        print(f"Reaction time: {reaction_time} ms")
        
        # Make game faster (minimum 0.2 seconds)
        delay_time = max(0.2, delay_time - 0.05)
        
        # Turn off LED
        leds[target_led].off()
        
        # Wait for button release
        while buttons[pressed_button].value() == 1:
            time.sleep(0.01)
        
        # Wait before next round (gets shorter)
        time.sleep(delay_time)
        
        return True
    else:
        # Wrong button!
        clear_screen()
        print("===== GAME OVER =====")
        print(f"\n✗ WRONG BUTTON!")
        print(f"You pressed button {pressed_button + 1}")
        print(f"Should have pressed button {target_led + 1}")
        print(f"\nFinal score: {score}")
        
        # Blink all LEDs to show error
        all_leds_off()
        time.sleep(0.5)
        blink_all_leds()
        
        return False

# Main game loop
print("===== MULTI-LED REACTION GAME =====")
print("\nRules:")
print("- Watch which LED lights up")
print("- Press the matching button as fast as you can")
print("- Game gets faster with each correct press")
print("- Wrong button = Game Over!")
print("\nLED 1 = Button 1")
print("LED 2 = Button 2")
print("LED 3 = Button 3")
print("LED 4 = Button 4")
print("\nStarting in 3 seconds...")

# Turn off all LEDs
all_leds_off()
time.sleep(3)

# Clear screen before starting
clear_screen()

# Game loop
game_running = True
while game_running:
    game_running = play_round()

# Game over
clear_screen()
print("\n===== GAME OVER =====")
print(f"Your final score: {score}")

# Give rating based on score
if score >= 20:
    print("\nAMAZING! You're a reaction champion!")
elif score >= 15:
    print("\nEXCELLENT! Super fast reflexes!")
elif score >= 10:
    print("\nGREAT JOB! Nice reflexes!")
elif score >= 5:
    print("\nGOOD EFFORT! Keep practicing!")
else:
    print("\nKeep trying! You'll get better!")

print("\nPress CTRL+C to exit or restart to play again")

# Keep all LEDs off at the end
all_leds_off()