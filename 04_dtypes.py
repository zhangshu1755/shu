'''
自定义复合类型
列与列之间可以为不同类型，同一列内类型必须相同
'''
import numpy as np
import warnings

warnings.filterwarnings('ignore')

data = [('zs',[100,100,100],18),
        ('ls',[90,90,90],19),
        ('ww',[80,80,80],20)]

# ary = np.array(data,dtype='U2,3i4,i4')
#
# print(ary['f2'].mean())
# print(ary['f1'].mean(axis=1))
# print(ary['f1'].mean(axis=0))

ary = np.array(data,
               dtype={'names':['name','score','age'],
                      'formats':['U2','3i4','i4']})

print(ary['age'])
print(ary['age'].mean())






