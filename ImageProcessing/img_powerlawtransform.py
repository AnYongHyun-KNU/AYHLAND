# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:57:00 2019

@author: pc
"""

# Power-Law Transformation
# Gamma Transformation
import math
import cv2 

# 그레이 이미지, 컬러 이미지 각각 읽어온 후 출력
img = cv2.imread('gamma.jpg',cv2.IMREAD_GRAYSCALE)

height,width = img.shape
gamma = float(input("감마변환, gamma 값 입력:")) # gamma, c 값 입력
c = float(input("감마변환, c값 입력:"))
cv2.imshow('original image',img) # 원 이미지 출력

max=0
min=255

# 감마 변환 후 최대/최소 찾기 
for y in range (0, height):
    for x in range(0, width):
        r= img.item(y,x)
        pixelvalue =c*(math.pow(r,gamma)) # 감마 변환 값 게산 
        if pixelvalue>max:
            max = pixelvalue
         
        if pixelvalue<min:
            min = pixelvalue
            
 # 감마 변환 값 정규화 및 원본 픽셀에 대입 
for y in range (0, height):
    for x in range(0, width):
        
        r= img.item(y,x) 
        s=c*(math.pow(r,gamma)) # 감마 변환 값 게산  (s= c*r^gamma)
        normalized_s=((s-min)/(max-min))*255  #range normalization 
        img.itemset(y,x,normalized_s) # 원본 픽셀에 정규화 감마 변환 값(s) 대입  
             
cv2.imshow(' Gamma Transformation',img) # 감마 변환 결과 출력        
     
    
            
        
cv2.waitKey(0)