from collections import deque
# a = ['s','u','s','h','r','e']
# d = deque(a)
# print(d)
from collections import ChainMap
a = {1: 'sushree', 2: 'sahoo'}
b = {1: 'sushree', 2: 'sahoo'}
c = ChainMap(a,b)
print(c)