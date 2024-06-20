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

compareIndex = [[18,4], [6,8], [10, 12], [14,16], [18,20]]
open = [False,False,False,False,False]
gesture = [[True, True, True, True, True, "Hi!"],
           [False, True, True, False, False, "V!"],
           [True, True, False, False, True, "SpiderMan!"],
           [True, False, False, False, False, "Good!"],
           [False, False, True, False, False, "Fuck!"],
           [True, False, False, False, True, "Promise Me!"],
           [True, True, False, False, False, "BANG!"],
           [False, False, False, False, False, "Danger"]]

def led_on(num):
    if(num == 0):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
    elif(num == 1):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
    elif(num == 2):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
    elif(num == 3):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
    elif(num == 4):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
    elif(num == 5):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)


def get_number(open):
    number = 0
    for i in range(0,5):
        if(open[i]):
            number = number + 1
    return number


while True:
    success,img = cap.read()
    h,w,c = img.shape
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
    results = my_hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for i in range(0,5):
                open[i] = dist(handLms.landmark[0].x,handLms.landmark[0].y, handLms.landmark[compareIndex[i][0]].x, handLms.landmark [compareIndex[i][0]].y) < dist(handLms.landmark[0].x,handLms. landmark[0].y,handLms.landmark [compareIndex[i][1]].x, handLms.landmark [compareIndex[i][1]].y)
            print(open)
            text_x = (handLms.landmark[0].x * w)
            text_y= (handLms.landmark[0].y *h)
            for i in range(0, len( gesture)):
                number = 0
                number = get_number(open)
                if(number!=0):
                    cv2.putText(img, "손가락 " + number + "개 폈네!", (round(text_x)-50, round(text_y) - 250),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
                    led_on(number)
                else:
                    cv2.putText(img, "손가락 한개도 안폈네!", (round(text_x)-50, round(text_y) - 250),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
                    led_on(number)


                # flag = True
                # for j in range(0,5):
                #     if(gesture[i][j] != open[j]): flag = False
                # if(flag == True):
                #     cv2.putText(img, gesture[i][5], (round(text_x)-50, round(text_y) - 250),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
                #     led_on(gesture[i][5])
                    # playsound.playsound (gesture[i][5]+'.mp3')
            mpDraw.draw_landmarks (img, handLms, mphands. HAND_CONNECTIONS)
    cv2.imshow("HandTracking", img)
    cv2.waitKey(1)
    GPIO.cleanup()