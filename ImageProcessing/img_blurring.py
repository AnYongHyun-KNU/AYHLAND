# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:57:44 2019

@author: pc
"""

import cv2
import numpy as np

img = cv2.imread('lena.jpg',cv2.IMREAD_COLOR)
height = img.shape[0]
width = img.shape[1]
result_img = np.zeros((height,width,3),np.uint8)

print(height, width)
cv2.imshow('original', img)

# 사용자로부터 평균 필터 마스크 사이즈 입력 받기 
while(1):
    n = int(input('평균 마스크(정방행렬) 사이즈 n 입력:'))
    if ((n%2)== 1):
        print('{0}x{0} 마스크 입니다.'.format(n) )
        break
    else:
        print('올바른 입력이 아닙니다.')
        
# 마스크 사이즈 별 패딩해야할 길이 계산 
# pSize = 1 or 2 or 3 ..... img[0:10,0:10,1]   result_img[0:10,0:10,1]
pSize=int(n/2) 

# 평균 마스크 (블러링 마스크)
meanMask=np.ones((n,n),np.float64)

# zero pedding 
zeroImg = np.zeros((height+(2*pSize),width+(2*pSize),3),np.float64)
zeroImg[pSize:width+pSize,pSize:height+pSize,:] = np.float64(img)  # 1:width+1 하면 1~width까지 슬라이싱 된다.   

# =============================================================================
#  n=3 일때 마스크 3x3이고, pSize = 1 
#  zeroImg.shape                                  type(zeroImg[100,100,1])
#  Out[10]: (514, 514, 3),인덱싱513까지 존재       Out[14]: numpy.float64
# =============================================================================


for y in range(0,height):
    for x in range(0,width):
        for i in range(0,3):
            y_zeroImg = y+pSize # 원본이미지 y,x에 대응 되는, 제로 패 이미지의 좌표 
            x_zeroImg = x+pSize
            convResult= np.sum(zeroImg[y_zeroImg-pSize:y_zeroImg+pSize+1,x_zeroImg-pSize:x_zeroImg+pSize+1,i]*meanMask)# np에서 A * A는 원소별 곱셈  #!!! 슬라이싱 주의 +2 해야함 .
            result_img[y,x,i]= np.uint8(convResult/float(n*n)) 
      
# 결과 영상 출력        
cv2.imshow('original', img)
cv2.imshow('result', result_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)