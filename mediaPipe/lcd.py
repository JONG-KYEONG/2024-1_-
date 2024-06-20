import cv2
import mediapipe as mp
import math

import RPi.GPIO as GPIO
import time

# from gtts import gTTS
# import playsound

cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
my_hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

GPIO.setmode(GPIO.BCM) #BCM(BCM GPIO 기준), BOARD(보드 핀 번호 기준)
GPIO.setup(16, GPIO.OUT) # 
GPIO.output(16, GPIO.LOW)
GPIO.setup(17, GPIO.OUT) # 
GPIO.output(17, GPIO.LOW)
GPIO.setup(18, GPIO.OUT) # 
GPIO.output(18, GPIO.LOW)
GPIO.setup(19, GPIO.OUT) # 
GPIO.output(19, GPIO.LOW)
GPIO.setup(20, GPIO.OUT) # 
GPIO.output(20, GPIO.LOW)

def dist(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1 - x2, 2)) + math.sqrt(math.pow(y1 - y2, 2))
	@@ -35,18 +40,19 @@ def dist(x1,y1,x2,y2):
           [True, True, False, False, False, "BANG!"],
           [False, False, False, False, False, "Danger"]]

def led_on(text):
    if(text == "Danger"):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
    elif(text == "Hi!"):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)


while True:
	@@ -67,7 +73,7 @@ def led_buzzer(text):
                    if(gesture[i][j] != open[j]): flag = False
                if(flag == True):
                    cv2.putText(img, gesture[i][5], (round(text_x)-50, round(text_y) - 250),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
                    led_on(gesture[i][5])
                    # playsound.playsound (gesture[i][5]+'.mp3')
            mpDraw.draw_landmarks (img, handLms, mphands. HAND_CONNECTIONS)
    cv2.imshow("HandTracking", img)






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
