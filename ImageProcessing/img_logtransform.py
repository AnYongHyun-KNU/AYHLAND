# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:48:50 2019

@author: pc
"""
import cv2
import math
import numpy as np
# Intensity transformation - (2) Image log transformation

# Q 255넘어가면 ?...
img = cv2.imread('fspectrum.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('original',img) #GRAY로 이미지 읽은 후 출력 

height =img.shape[0]  #이미지 크기 저장 
width = img.shape[1]
new_img=np.zeros((height,width),np.float32) 
min=255.0;
max=0.0;
# 로그 변환 후 최대 최소 값 찾기 
for y in range (0, height):
    for x in range(0, width):
        r=np.float32(img[y,x])  # <class 'numpy.float32'>, 
        s = (math.log10(1+r)) # 로그 변환, s=c*log10(1+r)  <class 'float'>
        if s > max:
            max = s
         
            
        if s <min:
            min = s
            
        new_img[y,x] = s #float32로 배열만들었기 때문에 type(new_img[y,x]) = type(new_img[y.x])
                       # 만들어진 np배열에 맞게 들어감, 위에서 np.unit8하니 uint8로 됨. 
                       
normalized_new_img = np.uint8((((new_img-min)/(max-min))*(255.0-0.0) + 0.0)) # range normalization , 마지막에 np.uint8로 변환 


cv2.imshow('log transformation',normalized_new_img) # 로그 변환 이미지 출력

cv2.waitKey(0)