import numpy as np
import matplotlib.pyplot as plt
import cv2
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
img=plt.imread("n.jpg")
plt.imshow(img)
img.shape
img1=img.copy()
eye=eye_cascade.detectMultiScale(img1)[0]
#print (eye)
eye_x,eye_y,eye_w, eye_h= eye
img = cv2.rectangle(img, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (255,255,255), 5 )
plt.imshow(img)

glasses=plt.imread("sun-glasses.png")
glasses.shape

glasses=cv2.resize(glasses,(eye_w+60,eye_h+55))
glasses.shape

for i in range(glasses.shape[0]):
  for j in range(glasses.shape[1]):
    if (glasses[i,j,3]>0):
      img1[eye_y+i-25,eye_x+j-12, :]=glasses[i,j,:-1]
      
plt.imshow(img1)
#plt.imshow(img)

