import numpy as np
import cv2 as cv
import sys 
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 16
GPIO.setup(PIR_PIN, GPIO.IN)
camera = PiCamera()


try:
    print("Starting Up")
    sleep(2)
    print("Ready")
    i = 0
    while True:
        if GPIO.input(PIR_PIN):
            with open("" + str(i) + ".jpg", "w") as file:
                camera.capture(file.name)
                img = cv.imread(file.name)
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
	                cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	                roi_gray = gray[y:y+h, x:x+w]
	                roi_color = gray[y:y+h, x:x+w]
	                eyes = eye_cascade.detectMultiScale(roi_gray)
	                for (ex,ey,ew,eh) in eyes:
		                cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                cv.destroyAllWindows()
                cv.imshow('img',img)
                sleep(10)
                cv.waitKey(0)

                for x in range(20):
                    if (GPIO.input(PIR_PIN)):
                        mot += 1
                while  mot > 0:
                    sleep(2)
                    print("Motion detected:" + str(i)) 
                    mot = 0
                    for x in range(20):
                        if (GPIO.input(PIR_PIN)):
                            mot += 1
            camera.stop_recording()
            i += 1
            print("incremented" + str(i))
except Exception as ex:
    print("This didn't work. %s" % ex)
finally:
    camera.close()













