#coding:utf-8
import math
import pandas as pd
#df=pd.read_csv('./test.csv')
#print(df.head(5))
df=pd.read_csv('test.csv',usecols=['battle_type','interval'])
#print(df)
num1=df['battle_type'].value_counts()
'''
 print(num1)
 1    137965
 6     43996
 8     42947
 2     22482
 5     11901
 4      8851
 3       153
 9         1
 dtype: int64
'''
#print(str(df['battle_type'].dtypes))
#print(str(df['interval'].dtypes))
'''
print("战斗类型1")
print("最大：",end='')
print(df[df['battle_type']==1]['interval'].max())
print("最小：",end='')
print(df[df['battle_type']==1]['interval'].min())
print("均值：",end='')
print(df[df['battle_type']==1]['interval'].mean())
print("方差：",end='')
print(df[df['battle_type']==1]['interval'].std())
'''
types=pd.Series(df['battle_type']).unique()
#print (types)
#[1 6 2 5 4 8 3 9]
types.sort()
'''
for n in num1:
    print(n)

137965
43996
42947
22482
11901
8851
153
1
'''
for n in types:
    s="战斗类型：{name}"
    print(s.format(name=n))
    print("最大：",end='')
    print(df[df['battle_type']==n]['interval'].max())
    print("最小：",end='')
    print(df[df['battle_type']==n]['interval'].min())
    print("均值：",end='')
    print(df[df['battle_type']==n]['interval'].mean())
    print("方差：",end='')
    tmp=df[df['battle_type']==n]['interval'].std()
    print(0 if math.isnan(tmp) else tmp)
    print('-'*20)
