# import RPi.GPIO as GPIO
# from RPLCD.gpio import CharLCD
# import time

# # Define the pin configuration
# LCD_RS = 11
# LCD_E = 10
# LCD_D4 = 6
# LCD_D5 = 5
# LCD_D6 = 4
# LCD_D7 = 1

# # Setup GPIO mode
# GPIO.setmode(GPIO.BCM)


# # Initialize the LCD
# lcd = CharLCD(
#     numbering_mode=GPIO.BCM,
#     cols=16, rows=2,
#     pin_rs=LCD_RS, pin_e=LCD_E,
#     pins_data=[LCD_D4, LCD_D5, LCD_D6, LCD_D7]
# )

# # Display text on the LCD
# lcd.write_string('HELLO WORLD')

# # Wait for user input
# input("Press any key to continue...")

# # Clear the LCD
# lcd.clear()

# # Cleanup GPIO
# GPIO.cleanup()

import wiringpi as wp
from time import sleep

LCD_RS = 11
LCD_E = 10
LCD_D4 = 6
LCD_D5 = 5
LCD_D6 = 4
LCD_D7 = 1

# Initialize wiringPi
wp.wiringPiSetup()

# Initialize the LCD
lcd = wp.lcdInit(2, 16, 4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 0, 0, 0, 0)

if lcd == -1:
    print("lcd init failed!")
    exit(1)

# Set the cursor to the first position (0, 0)
wp.lcdPosition(lcd, 0, 0)

# Print the message to the LCD
wp.lcdPuts(lcd, "HELLO WORLD")

# Wait for user input
input("Press Enter to clear the LCD...")

# Clear the LCD
wp.lcdClear(lcd)
