import os
import numpy as np 

#implementing the dimensions and shape

a = np.array([[[1,2,3,9],[4,5,6,9],[8,9,5,9]]
             ,[[11,12,13,19],[14,15,16,19],[18,19,15,19]]])
print('shape of a',a.shape)
print('shape of a[0]',a[0].shape)
print('shape of a[1]',a[1].shape)
print('length shape of a',len(a.shape))
print('size of a[0]',a[0].size)
print('size of a[1]',a[1].size)
print('size of a',a.size)
print('elements of a[0]',a[0])
print('elements of a[1]',a[1])
print('dimension of a',a.ndim)
