import cv2
import mediapipe as mp
import serial
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
mySerial = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
while True :
  sucess , img = cap.read()
  frame = cv2.flip(img,1)
  hands,img = detector.findHands(frame,flipType=False)
  if hands:
    hand1 = hands[0]
    lmlist1 = hand1["lmList"]
    bbox1 = hand1["bbox"]
    centerPoint1 = hand1["center"]
    handtype1 = hand1["type"]

    fingers1 = detector.fingersUp(hand1)
    if fingers1[0]==0 :
      mySerial.write(bytes('1', 'utf-8'))
    else:
      mySerial.write(bytes('0', 'utf-8'))

    if fingers1[1]==1 :
      mySerial.write(bytes('3', 'utf-8'))
    else:
      mySerial.write(bytes('2', 'utf-8'))
    if fingers1[2]==1:
      mySerial.write(bytes('5', 'utf-8'))
    else:
      mySerial.write(bytes('4', 'utf-8'))
    if fingers1[3]==1 :
      mySerial.write(bytes('7', 'utf-8'))
    else:
      mySerial.write(bytes('6', 'utf-8'))

    if fingers1[4]==1 :
      mySerial.write(bytes('9', 'utf-8'))
    else:
      mySerial.write(bytes('8', 'utf-8')) 
  cv2.imshow('image',img)    
  cv2.waitKey(1)
