import cv2
import mediapipe as mp
import math

import RPi.GPIO as GPIO


cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
my_hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT) 
GPIO.output(16, GPIO.LOW)
GPIO.setup(17, GPIO.OUT) 
GPIO.output(17, GPIO.LOW)
GPIO.setup(18, GPIO.OUT) 
GPIO.output(18, GPIO.LOW)
GPIO.setup(19, GPIO.OUT) 
GPIO.output(19, GPIO.LOW)
GPIO.setup(20, GPIO.OUT) 
GPIO.output(20, GPIO.LOW)

def dist(x1,y1,x2,y2):
    return math.sqrt(math.pow(x1 - x2, 2)) + math.sqrt(math.pow(y1 - y2, 2))

compareIndex = [[18,4], [6,8], [10, 12], [14,16], [18,20]]
open = [False,False,False,False,False]

def led(open):
    base = 16
    text = ""
    for i in range(0,5):
        if(open[i]):
            GPIO.output(base+i, GPIO.HIGH)
            text = text + str(i) + " "
        else: 
            GPIO.output(20, GPIO.LOW)
    text = text + ""
    return text



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
            text = led(open)
            cv2.putText(img, text, (round(text_x)-50, round(text_y) - 250),cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
            mpDraw.draw_landmarks (img, handLms, mphands. HAND_CONNECTIONS)
    cv2.imshow("HandTracking", img)
    cv2.waitKey(1)