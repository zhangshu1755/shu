'''
数组的维度操作
'''
import numpy as np

#视图变维
ary = np.arange(1,10)

bry = ary.reshape(3,3)
bry[0][0] = 666

print(ary)
print(bry)

print(bry.ravel())
print(bry)

#创建3行3列的数组

#复制变维
ary = np.arange(1,10).reshape(3,3)

bry = ary.flatten()
bry[0] = 666
print(bry)
print(ary)

#就地变维
ary = np.arange(1,10)

ary.resize(3,3)
print(ary)






