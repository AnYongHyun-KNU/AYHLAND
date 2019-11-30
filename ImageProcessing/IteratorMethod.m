function thresh = test2(gray_img)
%% ����ó�� HOMEWORK2 2015112666 �ȿ���

% 'Iterator Selection Histogram' Method
% (Iterator threshold determation Method)
% fuction : calculate thresh, and convert rgb2binary using the calculated thresh
sum=0;
[ X, Y ] = size(gray_img);
img_size=X*Y;

% calculate first thershold value
for i= 1:X
    for j= 1:Y
        sum= sum + double(gray_img(i,j));
 
    end
end
newthresh=sum/img_size;

% thershold value ��� �ݺ�
while(1)
    highcount=0; % ��ġ�߿�
    lowcount=0;
    highsum=0;
    lowsum=0;
    for i= 1:X
        for j= 1:Y
            if (newthresh<gray_img(i,j))
                highcount=highcount+1;
                highsum= highsum+double(gray_img(i,j));
            else
                lowcount=lowcount+1;
                lowsum=lowsum+double(gray_img(i,j));
            end
        end
    end
    
    highthresh=highsum/highcount;
    lowthresh=lowsum/lowcount;
    oldthresh=newthresh;
    newthresh=(highthresh+lowthresh)/2; %calculate threshold value
    
    er=((newthresh-oldthresh)/newthresh)*100; %calculate realtive error
    
    if((abs(er)<0.0001)) % ������ ���� �������Ϸ� �پ��� (threshold���� ��ȭ�� ������)
        % ��� �ߴ�(while�� Ż��)
        break;
    end
end

thresh=newthresh; % final threshold value
nthresh=newthresh/255; %calculate normalized threshold
binary_img=im2bw(gray_img,nthresh);

subplot(1,2,1);
imshow(gray_img);
title('gray _ img')
subplot(1,2,2);
imshow(binary_img);
title(['Threshold' , num2str(newthresh)]);


