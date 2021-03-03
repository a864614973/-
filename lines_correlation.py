import pandas as pd
from sklearn import preprocessing
import numpy as np

data=pd.read_csv('data.csv',encoding = 'gb2312')
data=data.iloc[9:,1:12]
# print(data.columns)

data1=data.values

min_max_scaler = preprocessing.MinMaxScaler()
data_tra = min_max_scaler.fit_transform(data1)
data1 =pd.DataFrame(data_tra)
b=data1.corr()
print(data1.corr())
#由数据框调用corr方法,将会计算每个列两两之间的相似度，返回的是一个矩形
