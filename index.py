import numpy as np
import cv2
myrtmp_addr = "rtmp://luffy.ee.ncku.edu.tw:21935/live/a"
cap = cv2.VideoCapture(myrtmp_addr)

var_int_x = 100
var_int_y = 100

while True:
    ret, frame = cap.read()
    #Get frame height and width to access pixels
    height, width, channels = frame.shape

    #Accessing BGR pixel values    
    for x in range(0, width) :
        for y in range(0, height) :
            print (frame[var_int_x,var_int_y,0]) #B Channel Value
            print (frame[var_int_x,var_int_y,1]) #G Channel Value
            print (frame[var_int_x,var_int_y,2]) #R Channel Value