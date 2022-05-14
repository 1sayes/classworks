import matplotlib.axis
import numpy as np
a=np.ones((4,5))
print(a)

print(a.ndim)
print(a.shape)
print(a.itemsize)

b=np.diag([1,2,3,4])
print(b)
print(b[::2,::3])

c=np.arange(10)
d=c[3:7]
print(d)
d[:]=0
print(d)
print(c)
print(b.flags.owndata)

e=np.random.rand(3,5)
print(e)

print(e.sum())
print(e.sum(axis=0))
print(e.sum(axis=1))

a1=np.array([0,1,2,3,4])
b1=np.array([10])
c1=a1+b1
print(c1)

a2=np.array([[0,1],[2,3],[4,5]])
b2=np.array([[10],[20],[30]])
c2=a2+b2
print(c2)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
