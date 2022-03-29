from time import perf_counter
from pycat.extensions.turtle import Turtle
from pycat.core import Window

t1 = perf_counter()
for i in range(10000000):
    pass
t2 = perf_counter()
print('i:', t2-t1)

t1 = perf_counter()
for _ in range(10000000):
    pass
t2 = perf_counter()
print('_:', t2-t1)
