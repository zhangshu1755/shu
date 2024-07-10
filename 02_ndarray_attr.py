'''
ndarray数组的基本属性
'''
import numpy as np

#shape
ary = np.arange(1,9)
print(ary) ## [1 2 3 4 5 6 7 8]
print(ary.shape) #(8,)
#将一维数组转换为二维数组
ary.shape = (2,4) #(4,2) (8,1) (1,8)
print(ary)
#转换为三维
ary.shape = (2,2,2)#(1,1,8) (1,8,1)
print(ary)

print('==' * 30)

#dtype
ary = np.array([1,2,3,4,5],
               dtype='int32')
print(ary)
print(ary.dtype)

ary = ary.astype('float32')
print(ary)


#size
ary = np.arange(1,9)
print(ary.size) #8
ary.shape = (2,2,2)
print(ary.size) #8

print(len(ary))
print(ary)


#index索引
ary = np.arange(1,19)
ary.shape = (2,3,3)
print(ary)

print(ary[0])
print(ary[0][0])
print(ary[0][0][0])
#三维数组[页，行，列]
print(ary[0])
print(ary[0,0])
print(ary[0,0,0])

a = ary
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i, j, k])

# ary = np.array([1,2,3,4,5],dtype=np.bool_)
# ary = np.array([1,2,3,4,5],dtype='bool_')
# ary = np.array([1,2,3,4,5],dtype='bool')
ary = np.array([1,2,3,4,5],dtype='?')
print(ary)


ary = np.array(['zcm','qwer',
                'abcdefghijklmn'])
print(ary.dtype)  # <U14
print(ary.itemsize)#一个元素所占的字节大小
print(ary.nbytes)#总字节数

