# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:43:41 2019

@author: pc
"""

import numpy as np
from matplotlib import pyplot as plt #다 이거씀 
import cv2 


# numpy 자료형은 int32 unit8이런거고 그냥 일반 파이썬 자료형은 숫자붙는 건 따로 없고 인트 더블이런거인듯
# r g b의 히스토그램은 밝기 값이 아니라 색상 값임 


img = cv2.imread('lena.jpg',cv2.IMREAD_COLOR)
channel= ('b','g','r')

bins = np.zeros((256,3), np.int32) #괄호 빼면 안된다. 

for i, ch in enumerate(channel): 
    for pixel in range(0,256):
        
        for y in range(0,img.shape[0]):
            for x in range(0,img.shape[1]):
                if img.item(y,x,i)==pixel:
                    bins[i,pixel]=+1

blue_bin=bins[:,0] # 차원과 달리 0부터 임에 주의. . reshape 사용 가능                     
green_bin=bins[:,1]
red_bin=bins[:,2]
print(type(blue_bin), blue_bin.shape) 

#계산 된 히스토그램 값 출력 
plt.subplot(2,2,1)
plt.imshow(img)  #뒤에는 컬러 공간 img,'gray'
plt.title('img')       
                  
plt.subplot(2,2,2)
plt.plot(hist1,color='b')
plt.title('b histogram') 

plt.subplot(2,2,3)
plt.plot(hist2,color='g')
plt.title('g histogram')          

plt.subplot(2,2,4)
plt.plot(hist3,color='r')
plt.title('r histogram') 
plt.tight_layout() # 간격 맞춰주기
plt.show()


                   
    

 #되는 코드
#bins = np.zeros((3,256), np.int32)
#for i in range(0,30):
#    bins[i]+=1
#
#print(bins[1,100])