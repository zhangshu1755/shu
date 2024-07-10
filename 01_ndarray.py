'''
创建ndarray对象
'''
import numpy as np

#np.array
ary = np.array([1,2,3,4,5,6])
print(ary)
print(type(ary))

#广播机制
print(ary + 1)
print(ary * 2)
print(ary == 3)
print(ary * ary)

#np.arange(可以生成浮点数)
ary = np.arange(0.1,1.1,0.1)
print(ary)

ary = np.array([1,100,200,300,400],
               dtype='int64')
print(ary)

#np.zeros
zeros = np.zeros(shape=(3,3),
                 dtype='int32')
print(zeros)

#np.ones
ones = np.ones(shape=(3,3),
               dtype='float32')
print(ones)

#np.zeros_like   np.ones_like

# [0,0,0,0,0]
zeros_like = np.zeros_like(ary)
print(zeros_like)


#生成shape=(18,) 值为0.2的数组

ary = np.zeros(shape=(18,),
                 dtype='float32') + 0.2
print(ary)