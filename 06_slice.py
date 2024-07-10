'''
数组的切片
'''
import numpy as np

ary = np.arange(1,19).reshape(3,6)
print(ary)
#前两行 ary[行的切片，列的切片]
print(ary[:2])
#前两行的前两列
print(ary[:2,:2])

#最后一行的最后一列
print(ary[-1:,-1:])
print(ary[-1:,-1])
print(ary[-1,-1])

#练习：
ary = np.arange(1,51).reshape(5,10)

#所有行，不要最后一列（二维）
print(ary[:,:-1])
#所有行，只要最后一列 (一维)
print(ary[:,-1])


