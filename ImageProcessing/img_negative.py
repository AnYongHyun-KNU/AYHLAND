# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:15:28 2019

@author: pc
"""
#그레이로 저장된이미 그냥 읽으면 rgb로 읽혀오고
#print(img[1,1]) 하면 [134,134,134] 나옴 

#Intensity transformation - (1) Image Negative 
import cv2
import numpy as np


# 그레이로 이미지 읽어오기 
img=cv2.imread('butterfly.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('butterfly.jpg(original)', img) # 원 이미지 출력

# 이미지 배열 크기 저장 
height, width = img.shape # numpy 함수, 차원을 튜플로 반환 
print(height) #236
print(width) #354

# 각 픽셀에 접근하여 Image Negative 변환 
for y in range (0,height):
    for x in range(0,width):
        r = img.item(y,x) # 각 화소 값 저장 
        img.itemset(y,x,(255-r)) #  s= L-1 - r (L : range [ex]356 ) 
        
cv2.imshow('img negative', img) # 변환 된 이미지 출력 
cv2.waitKey(0) # 입력한 'ms'만큼 사용자의 키보드 입력대기 

