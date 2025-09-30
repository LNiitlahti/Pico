# task1_print_numbers.py - Print numbers 0-9 (C) Lassi Niitlahti

# This program prints numbers from 0 to 9
# Simple loop to demonstrate basic Python programming on Pico

import time

# Loop through numbers 0 to 9
for i in range(10):
    print(i)
    time.sleep(0.5)  # Pause for half a second between prints

# Print completion message
print("Done printing numbers!")