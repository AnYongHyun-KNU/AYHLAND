# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:16:35 2019

@author: pc
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:21:14 2019

@author: pc
"""
import numpy as np
import cv2 #import cv2 as cv


#픽셀에 접근

redbox=cv2.imread('redbox.jpg',cv2.IMREAD_COLOR) # 좌표 순서가 (y,x)임에 주의 
cv2.imshow('original',redbox)
print(redbox[50,50])  # 출력결과 : [154 41 38] , 리스트 인덱싱 처럼 '[]'


#픽셀에 접근하여 수정하기 (흰점 찍기)

redbox[50,50]=[255,255,255] 
print(redbox[50,50]) # 출력 결과 : [255,255,255]
cv2.imshow('result1',redbox)


#red 색감 모두 없애기

redbox[:,:,2]=0   
cv2.imshow('result2',redbox)

# item. itemset을 이용하는 것이 더 빠르다. 픽셀 값 전체가 아닌 개별 요소로접근

redbox.itemset(60,60,0,255) # (60,60)의 blue 채널값을 255로 set
redbox.itemset(60,60,1,255) # (60,60)의 green 채널값을 255로 set
redbox.itemset(60,60,2,255) # (60,60)의 red 채널값을 255로 set
cv2.imshow('result3',redbox)

#이미지 픽셀접근으로 수직선과 수평선 그리기
# -> 중첩 포문 이용 
height = redbox.shape[0] # for y in range (0, hight)
width = redbox.shape[0] # for x in range(0,width)
# h, w, channel = redbox.shape

#이미지에서 일정부분 떼서, 다른 부분에 붙이기 
copy= redbox[0:30,0:50]
redbox[20:50,20:70]=copy
#cv2.imshow('copy', redbox)

#위 영역에 사각형그리기 참고 사각형 컬러 (255,0,0)= 빨강 
# 양끝 대각선의 좌표(왼쪽위/오른쪽아래)(임. 맨뒤에 1은 선의 두께.
# (x,y)임 
cv2.rectangle(redbox,(0,0),(50,30),(255,255,255),1)
#cv2.imshow('copyt and reccv2.waitKey(0) # 입력한 'ms'만큼 사용자의 키보드 입력대기 

cv2.waitKey(0)


