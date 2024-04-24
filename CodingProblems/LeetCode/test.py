from operator import itemgetter
import numpy as np
from itertools import combinations


dic = {1: 2, 3 : 4, 4: 5}
dic.values
print ((itemgetter(*[1])(dic)))
print(float('inf') == float('inf'))

a = np.array([0]*12)
len(a)

a = [1,2,3,4,5]
a[2:] = 5
print(a)