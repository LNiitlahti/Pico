# task2_name_checker.py - Asks for user's name and checks if they are Clark Kent (C) Lassi Niitlahti

# This program asks the user for their name
# If the name is "Clark Kent", it prints a special message
# Otherwise, it prints a different message

import time

#Small delay to ensure serial connection
time.sleep(1)

# Ask user for their name
name = input("What is your name? ")

# Check if the name is Clark Kent
if name == "Clark Kent":
    print("You are the Superman!")
else:
    print("You are an ordinary person.")