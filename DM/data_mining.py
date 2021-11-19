#将json字符串转换成python字典对象
import json
path='ch02/usagov_bitly_data2012-03-16-1331923249.txt'
#records=[json.loads(line) for line in open(path)]

#计数
def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts

#得到前十位
def top_counts(count_dict,n=10):
    value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort() #升序排序
    return value_key_pairs[-n:]

#sort与sorted的区别
#sort是list的成员函数，sorted是built-in函数，sort是在原位重新排列列表，而sorted()是产生一个新的列表。
print(sorted([5, 2, 3, 1, 4], reverse=True))
L = [('d',2),('a',4),('b',3),('c',2)]
print(sorted(L, key=lambda x:(x[1],x[0]), reverse=False))

#DataFrame是pandas中最重要的数据结构，它用于将数据表示为一个表格。
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
frame=DataFrame(records)
tz_counts=frame['tz'].value_counts() #降序排序
tz_counts[:10]

x='cvjasb ack  ajsk a dja  ka c'
print(x.split())

import numpy as np
data1=[6,7.5,8,0,1]
arr1=np.array(data1)
data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
data3=np.zeros((2,3))
data4=np.ones((2,3))
data5=np.arange(10)
data6=np.zeros_like(data2)
data7=np.eye(4)#主对角线全1，从左上角到右下角
data8=np.identity(4)#主对角线全1，从左上角到右下角

#数据类型转换
arr=np.array([1,2,3,4,5])
float_arr=arr.astype(np.float64)
float_arr=arr.astype(float)
numeric_strings=np.array(['1.25','-9.6','42'],dtype=np.string_)
numeric_strings.astype(float)

#基本的索引和切片 数组切片是原始数据的视图，数据不会被复制，视图上的任何修改都会直接反映到源数组上。
arr=np.arange(10)
arr_slice=arr[5:8]
arr_slice[1]=12345
arr
arr2=arr[5:8].copy() #显式复制