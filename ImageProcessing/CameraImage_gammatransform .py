# -*- coding: utf-8 -*-
#11월 25일 최종본 
"""
Created on Sun Nov 17 20:38:12 2019

@author: pc
"""
# 카메라 영상을 실시간으로 읽어와 감마 변환하기
# 웹캠 영상을 이용한 감마 변환

import cv2
import numpy as np
import math

 # 영상 밝기 평균 계산 
def Mean_Image(image):
    img_height, img_width = image.shape
    sum_value = 0.0
    for y in range(0,img_height):
        for x in range(0,img_width):
            sum_value += np.float64(image[y,x])
    
    mean_value = (sum_value)/(float(img_width*img_height))
    
    return mean_value

# 영상의 평균 밝기를 이용해 적절한 감마값 계산
def Calc_Gamma(mean):
   if (110 >= mean):
            gamma= (1/30)*(110-mean) + 1   #(3-1)/(60)*(110-mean) + 1
            gamma = 1/gamma
            if (gamma < 0.3): # 최소감마제한
                gamma=0.3
   elif (mean > 140):
            gamma = (1/20)*(mean-140) + 1 # ((2-1)/20)*(mean-140)+1    # 0.3의 역수 = 3 (감마 세트)
            if (gamma > 2): # 최대 감마 제한 
                gamma=2
   else:
       gamma=1
   return gamma #이거 빼먹는 실수 

# 카메라 영상을 실시간으로 읽어와 감마 변환하기

# 카메라에 접근하기 위해 VideoCapture 객체 생성
capture = cv2.VideoCapture(1)

# 0: 내장카메라, 1~n:외장카메라 처음에 1넣었는데 안되더라 ,, 웹캠 개수따라 0,1인듯  
# 저장되어있는 비디오파일 재생 cap = cv2.VideoCapture('video.mp4')


# 카메라의 다양한 속성 출력 
print('width :%d, height : %d' % (capture.get(3), capture.get(4))) # get안에 CAP_PROP~~해도된다. 
# width = 640, height = 480 
# dafault가 640 x 480 인듯. 출력 값도 그렇고, 밑에 set안해도 영상 그대로나오더라.
# set해서 크기 바꾸니 프레임 출력 화면크기 커짐, 
# 기본 크기? 640x480보다 크게는 안되고 작게(100x100)는 된다. 

#capture.set(option,n) , 카메라 속성 설정 
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640 )
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480 )
capture.set(3,640)
capture.set(4,480)
width = int(capture.get(3))
height = int(capture.get(4))

## 중요.'float' object cannot be interpreted as an integer 에러뜸
# np의 행렬 차원 수에는 정수가 들어갸아하는디 type -> height, width가 float 형임 
result_img = np.zeros((height,width,3),np.uint8) # 감마 변환 결과
result_v= np.zeros((height,width),np.float64) # Y채널 변환 결과 
frame_v = np.zeros((height,width),np.uint8)       
result_y= np.zeros((height,width,1),np.float64) # Y채널 변환 결과 
count=0
while(1):
    mode = input("측광 모드를 입력하세요 , '평균측광' or '중앙중점측광': ")
    if (mode =='평균측광') or (mode == '중앙중점측광'):
        print("%s모드입니다" %mode)
        break
    else:
        print("올바르지 않은 입력입니다.:")
#비디오 캡쳐 및 이미지 처리 
while (capture.isOpened()):    # while(1)해도 되긴 함 .
    ret, frame = capture.read() # 카메라의 상태(정상시 ret=1)와 프레임(현재의 프레임)을 받아옴    # fream을 이미지 처럼 사용 가능!
    print(frame.shape) # (480, 640, 3) 화면 해상도 100,100 set하니 120x160x3으로 들어옴. 뭔가 알맞게 조정하나 봄
    print(type(frame)) # <class 'numpy.ndrray'>         
    if (ret == False):
        print("카메라 오류")
        break
#    if ( capture.get(1) % 20 == 0 ):
#        count += 1
#        cv2.imwrite("frame%d.jpg" %count,frame)
    
    
    # YUV로 변환 후 채널 분리 및 밝기 평균 계산 
    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  
    #cv2.imshow("hsv", frame_hsv) #당연히 출력 이상하게됨. rgb기준으로 띄우니까 

    #HSV 채널의 범위 조사해보기 (언어마다 다름) 파이썬 h는 180인데 다른 언어 255로 정규화 된 경우도
    frame_h= frame_hsv[:,:,0]
    frame_s= frame_hsv[:,:,1]
    frame_v= frame_hsv[:,:,2] 
    
    if (mode== '평균측광'):
        mean_value = Mean_Image(frame_v)
    # 밝기 평균 계산 
    else:
        roi= frame_v[120:360,160:480]
        mean_value = Mean_Image(roi)
    
    # 흰/검은 채도가 없는건 같고 밝기의 차이 , 빨간색에서 채도가 낮아지면 밝기는 그대로고 분홍~갈색 ~ 흰색  
    gamma = Calc_Gamma(mean_value) # 밝기에 따른 감마값 계산
    print('평균 밝기: {0}감마 값 : {1}'.format(mean_value,gamma))   # 계산시 25.0 이런거 했으면 굳이 float64 안해도 됨 마지막에 imshow할때 uint8만하면 된다. 
                                          # ps 아웃라이어 제거하는 법. min의 10 퍼센트 max의 10퍼센트를 본다.
                                          # 즉, 아웃라이어가 있으면 영상은 min max찾아서 normalize할 때나 255로 나누고 할때나 똑같다!!
                                          # min~max 범위를 늘리는 건 너무늘어나서 감마변환 효과가 줄어드는거고 0~1 최대최소값 임의로잡아주고 늘리는건
                                          # min~max 범위 입장에서는 별로안늘어남 
    result_v = (frame_v/255.0)**gamma
    # min/max 찾는 등의 경우는 반드시 for문 돌려야하지만, 이건 안돌려도 된다.     
       
 #   frame_v = (result_v - min_value)/(max_value - min_value) * 255.0
    # 이렇게 안하고 255로나누고 감마변환하면  0~1 range에 들어온다 거기 다시 255곱하면 직관적으로 그래프 1:1대응관계 볼 수 있어서
    # 자주 쓰임. 보통 로그/감마변환시 많이 쓰는 방법이며. min max 찾아서하면 감마 0.5넣어도 별로 안밝아짐. 왜냐하면 실컷 감마변환
    # 해놓은 거를 min max범위 양끝을 잡고 다시 0~255로 땡기니까 감마변환효과 줄어듬.
    frame_v = result_v * 255.0 # 이거는 0~1사이에 들어오니까 min max 안찾고 그냥 0,1을 min max로 박아버린 것.  그러므로 덜 땡겨짐.
    
    
    #큰 실수!!!!!!!!!!!!: for 문돌리면서  넘피배열전체 = 넘피배열원소한개(픽셀한개)  이런식으로 대입하는 실수.. 이미지 완전이상하게나옴 
   
    frame_hsv[:,:,2] = np.uint8(frame_v)
    
    # yuv를 다시 rgb로 변환
    result_img=cv2.cvtColor(frame_hsv,cv2.COLOR_HSV2BGR)
    if mode =='중앙중점측광':
        for y in range(120,360):
            result_img.itemset(y,160,0,0)
            result_img.itemset(y,160,1,0)
            result_img.itemset(y,160,2,255)
            result_img.itemset(y,480,0,0)
            result_img.itemset(y,480,1,0)
            result_img.itemset(y,480,2,255)

        for x in range(160,480):
            result_img.itemset(120,x,0,0)
            result_img.itemset(120,x,1,0)
            result_img.itemset(120,x,2,255)
            result_img.itemset(360,x,0,0)
            result_img.itemset(360,x,1,0)
            result_img.itemset(360,x,2,255)
                                     
    # 0.1 (평균값)  ~   1(128)    ~  10(256)   
    # 0.0005377x^{2}\ -0.06132813\ +\ 0.05                                             
    cv2.imshow("orginal frame", frame) 
    cv2.imshow("gamma tranform", result_img)    
    if cv2.waitKey(1) > 0:     # 0보다 크다했으므로 어떤 키를 눌러도 break 작동 
        break                  # waitkey(0)일 경우 지속적으로 검사하여 frame이 넘어가지 않음 ( while문 안돌아간다 )
   
  
     #dealy <=0 키 입력시 까지 무한 대기  , 키입력시 해당 키(ESC 엔터 등 )값 반환 
     #delay > 0 : 지연시간 동안 키 입력 대기, 지연시간 내에 키 이벤트 없으면 -1  반환키입력시 해당 키(ESC 엔터 등의 아스키 값 )값 반환 
     #cv2.waitKey(1)==ord(q): break  : q버튼누르면 종료
     
capture.release() # 카메라에서 받아온 메모리(객체) 제거  
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
