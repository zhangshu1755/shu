'''
掩码操作：布尔掩码，索引掩码
'''
import numpy as np

#布尔掩码
ary = np.array([100,200,300,400,500])
mask = [True,False,True,False,True]
print(ary[mask])

#生成1-100中3的倍数
ary = np.arange(1,101)
print(ary[ary % 3 == 0])

#生成1-100中能够同时被3和7整除的数字
ary = np.arange(1,101)
mask = (ary % 3 == 0) & (ary % 7 == 0)
print(ary[mask])

#索引掩码
ary = np.array(['bmw','audi','benz','BYD'])
# mask = [3,0,1,2]
# mask = [2,0]
mask = [3,3,3,0,1,3,3,1,1,0,2]
print(ary[mask])

