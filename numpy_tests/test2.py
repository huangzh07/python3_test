import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''

print(a.shape, a.ndim, a.itemsize, a.size, type(a))
#(3, 5) 2 4 15 <class 'numpy.ndarray'>

b = np.array([1,2,3,4], dtype='float64')
print(b)
print(b.itemsize)
