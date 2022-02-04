# 24.Write a Python program to multiply all the items in a list.
import functools
import math
import operator

list=[1,2,3]
print(functools.reduce(operator.mul, list, 1))
print(functools.reduce((lambda x, y: x * y),list))