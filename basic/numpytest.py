#!usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 20
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)

persontype = np.dtype(
    {
        'names':['name','age', 'chinese', 'math', 'english'],
        'formats':['S32', 'i', 'i', 'i', 'f']
    })
peoples = np.array([("zhangfei",32,74,100,90),("Guanyu",32,74,100,90),("liubei",35,74,100,90)],dtype=persontype)
ages = peoples[:]['age']
chineses= peoples[:]['chinese']
print(ages)
print(np.mean(ages))
print(np.mean(chineses))

x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.remainder(x1, x2))

##################
arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(arr3))
print(np.amin(arr3, 0))
print(np.amin(arr3, 1))

print(np.ptp(arr3,0))
print(np.ptp(arr3,1))
print(np.ptp(arr3))

print(np.median(arr3, axis=0))
print(np.median(arr3, axis=1))
print(np.mean(arr3,axis=0))
xran = range(1,11,2)
print(xran)
for i in xran:
    print(i)


