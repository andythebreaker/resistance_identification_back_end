import numpy as np
import cv2
import subprocess
from datetime import datetime

def normalize8(I):
  mn = I.min()
  mx = I.max()

  mx -= mn

  I = ((I - mn)/mx) * 255
  return np.round(I).astype(np.uint8)

def dateTimeNowStr():
    # datetime object containing current date and time
    now = datetime.now()
    
    print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    print("date and time =", dt_string)	
    return dt_string

myrtmp_addr = "rtmp://luffy.ee.ncku.edu.tw:21935/live/a"
#[REF]https://stackoverflow.com/questions/45993828/get-videostream-from-rtmp-to-opencv
cap = cv2.VideoCapture(myrtmp_addr)

var_int_x = 100
var_int_y = 100
img_arrayR = []
img_arrayG = []
img_arrayB = []

#[REF]https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
for i in range(0, 100): 

    #TODO:Error handling

    #[REF]https://stackoverflow.com/questions/55827496/how-to-read-pixels-from-a-specific-video-frame
    ret, frame = cap.read()
    #[REF]https://stackoverflow.com/questions/19181485/splitting-image-using-opencv-in-python
    b,g,r = cv2.split(frame)
    #b
    #[REF]https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html
    gray = np.float32(b)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    #[REF]https://shengyu7697.github.io/python-opencv-threshold/
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    img_arrayB.append(dst)
    #r
    gray = np.float32(r)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    img_arrayR.append(dst)
    #g
    gray = np.float32(g)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    img_arrayG.append(dst)
    #print(dst)
    #print(type(frame))

    #Get frame height and width to access pixels
    height, width, channels = frame.shape
    size = (width,height)

    #Accessing BGR pixel values    
    #for x in range(0, width) :
    #    for y in range(0, height) :
    #        print (frame[var_int_x,var_int_y,0]) #B Channel Value
    #        print (frame[var_int_x,var_int_y,1]) #G Channel Value
    #        print (frame[var_int_x,var_int_y,2]) #R Channel Value

#[REF]https://docs.opencv.org/ref/2.4/dd/d9e/classcv_1_1VideoWriter.html
out = cv2.VideoWriter(dateTimeNowStr()+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size,True)
print(size)

for i in range(len(img_arrayB)):
    #[REF]https://blog.csdn.net/weixin_43624538/article/details/87436154
    var_marged_rgb=cv2.merge([normalize8(img_arrayB[i]),normalize8(img_arrayG[i]),normalize8(img_arrayR[i])])
    #[REF]https://stackoverflow.com/questions/53235638/how-should-i-convert-a-float32-image-to-an-uint8-image
    out.write(var_marged_rgb)
out.release()