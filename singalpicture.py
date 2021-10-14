# imports
import numpy as np
import cv2
import subprocess
from datetime import datetime
# fucn.s
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

# golb
th_dst=0.04
# 讀取圖檔
img = cv2.imread('tp2.jpg')
b,g,r = cv2.split(img)
gray = np.float32(b)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
retB, dstB = cv2.threshold(dst,th_dst*dst.max(),255,0)
gray = np.float32(r)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
retR, dstR = cv2.threshold(dst,th_dst*dst.max(),255,0)
gray = np.float32(g)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
retG, dstG = cv2.threshold(dst,th_dst*dst.max(),255,0)
var_marged_rgb=cv2.merge([normalize8(dstB),normalize8(dstR),normalize8(dstG)])
cv2.imwrite(dateTimeNowStr()+'.jpg', var_marged_rgb, [cv2.IMWRITE_JPEG_QUALITY, 100])