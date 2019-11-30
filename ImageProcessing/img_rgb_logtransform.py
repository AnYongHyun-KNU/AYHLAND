# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:48:50 2019

@author: pc
"""
import cv2
import math
import numpy as np
# Intensity transformation - (2) Image log transformation
# rgb에서 밝기 정보만 분리해서 변환하기 

img = cv2.imread('nighthouse.jpg',cv2.IMREAD_COLOR)
cv2.imshow('orginal',img)

height,width,channel = img.shape
img_result = np.zeros((height,width,channel),np.uint8) #변환이미지 
y_result = np.zeros((height,width),np.float64) # y채널 변환 이미지, double 형 



# yuv로 변환 후 채널 분리 
yuv_img = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)

y_img=yuv_img[:,:,0]
u_img=yuv_img[:,:,1]
v_img=yuv_img[:,:,2]

#함수 이용 방법 
# =============================================================================
# b,g,r=cv2.split(img) # bgr로 분리함 
# 
# img1=cv2.merge([b,g,r]) #rgb하면 안됨 
# =============================================================================

#y채널에 접근하여 로그변환
max=0.0
min=255.0

for y in range (0, height):
    for x in range(0, width):
        r=np.float64(y_img[y,x])  # float64, double로 형변환 
        s = (math.log10(1+r)) # 로그 변환, s=c*log10(1+r)  s=<class 'float'>
        if s > max:
            max = s
        if s <min:
            min = s
            
        y_result[y,x] = s # y_result는 np.float64형 
                       
y_img = ((((y_result-min)/(max-min))*(255.0-0.0) + 0.0)) # uint8로 형변환 안해줘도 자동으로 된다, 이미 y_img는 unit형이라서 
#정규화

#yuv 채널 다시 합친 후, rgb로 변환 
img_result[:,:,0]=y_img
img_result[:,:,1]=u_img
img_result[:,:,2]=v_img
img_result=cv2.cvtColor(img_result,cv2.COLOR_YUV2BGR)

cv2.imshow('result', img_result)





cv2.waitKey(0)
