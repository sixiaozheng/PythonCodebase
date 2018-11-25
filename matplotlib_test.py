# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
#import numpy as np

x=[55*36,68*45,84*56,104*69,130*86,162*107,323*214,647*430,970*646,1132*755,1293*863,1455*972,1616*1080]
x1=[20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,105,110,115,120,125,130,135,140,145,150,155,160,165,170,175]
#seetaface
y1=[0.151616,0.280909,0.501551,0.871722,1.55025,2.55822,13.0583,59.4863,144.148,207.337,249.36,315.517,414.142]
#adaboost
y2=[0.0030745,0.0117585,0.0254166,0.024907,0.0400457,0.0534566,0.181143,0.639024,1.43475,1.97488,2.69486,3.34832,4.05964]
y3=[17.6821,12.6235,10.7166,9.00306,7.78206,6.45643,5.72534,5.26802,4.47978,4.00196,3.62765,3.19585,3.30025,2.88101,2.49772,2.30301,2.0649,1.95101,1.85531,1.6275,1.52504,1.43224,1.42617,1.22647,1.15637,1.07615,1.04837,0.911973,
    0.876854,0.83046,0.76954,0.71522,0.684497,0.649528,0.594229,0.582307,0.554261,0.510811,0.46977,0.459612,0.449573,0.393956,0.336829,0.321494,0.300858,0.258791,0.223782,0.232624,0.192389,0.168357,0.152265,0.15756,0.148112,
    0.120921,0.112637,0.130553]
plt.plot(x,y1,'b')
plt.title(u'基于漏斗结构级联的多视角人脸检测时间与像素的关系曲线',fontproperties='SimHei')
plt.xlabel(u'像素',fontproperties='SimHei')
plt.ylabel(u'检测时间',fontproperties='SimHei')

plt.figure(1)
plt.plot(x,y2,'r')
plt.title(u'基于Adaboost算法的人脸检测时间与像素的关系曲线',fontproperties='SimHei')
plt.xlabel(u'像素',fontproperties='SimHei')
plt.ylabel(u'检测时间',fontproperties='SimHei')

plt.figure(2)
l1,=plt.plot(x,y1,'b')
l2,=plt.plot(x,y2,'r')
plt.title(u'基于漏斗结构级联的多视角人脸检测时间和基于Adaboost算法的人脸检测时间与像素的关系曲线',fontproperties='SimHei')
plt.xlabel(u'像素',fontproperties='SimHei')
plt.ylabel(u'检测时间',fontproperties='SimHei')
plt.legend(handles = [l1, l2,], labels = ['Funnel-structured', 'adaboost'], loc = 'best')

plt.figure(3)
plt.plot(x1,y3)
plt.title(u'MinFaceSize与检测时间的关系曲线',fontproperties='SimHei')
plt.xlabel(u'MinFaceSize')
plt.ylabel(u'检测时间',fontproperties='SimHei')

plt.show()