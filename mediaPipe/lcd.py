import wiringpi as wp
import time

# Pin configuration using WiringPi numbering
LCD_RS = 11
LCD_E = 10
LCD_D4 = 6
LCD_D5 = 5
LCD_D6 = 4
LCD_D7 = 1

# Initialize WiringPi and LCD
wp.wiringPiSetup()

lcd = wp.lcdInit(2, 16, 4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 0, 0, 0, 0)
if lcd == -1:
    print("lcd init failed!")
else:
    # Clear the LCD screen before writing
    wp.lcdClear(lcd)
    
    # Display text on the LCD
    wp.lcdPosition(lcd, 0, 0)
    wp.lcdPuts(lcd, "HI PYTHON")
    
    # Wait for user input
    input("Press Enter to continue...")

    # Clear the LCD screen
    wp.lcdClear(lcd)








# import wiringpi as wp
# from time import sleep

# LCD_RS = 11
# LCD_E = 10
# LCD_D4 = 6
# LCD_D5 = 5
# LCD_D6 = 4
# LCD_D7 = 1

# # Initialize wiringPi
# wp.wiringPiSetup()

# # Initialize the LCD
# lcd = wp.lcdInit(2, 16, 4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 0, 0, 0, 0)

# if lcd == -1:
#     print("lcd init failed!")
#     exit(1)

# # Set the cursor to the first position (0, 0)
# wp.lcdPosition(lcd, 0, 0)

# # Print the message to the LCD
# wp.lcdPuts(lcd, "HELLO WORLD")

# # Wait for user input
# input("Press Enter to clear the LCD...")

# # Clear the LCD
# wp.lcdClear(lcd)
