'''
时间日期类型
'''
import numpy as np


# 'YYYY-MM-DD hh:mm:ss'
data = ['2021','2022-01-01',
        '2023-01-01 08:08:08',
        '1970-01-01 00:00:00',
        '1970-01-02 00:00:00']

ary = np.array(data)
print(ary,ary.dtype)
#转换为时间日期类型

ary = ary.astype('datetime64[s]')
# ary = ary.astype('datetime64[D]')
print(ary)
print(ary.dtype)

#转成数值类型
ary = ary.astype('int32')
print(ary)





