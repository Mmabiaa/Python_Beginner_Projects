import math
from turtle import *

def heart(x):
    return 12*math.sin(x) ** 3

def show(x):
    return 12 * math.cos(x) - 5 * math.cos(2 * x) - 2 * math.cos(4 * x)

speed(0)
bgcolor('black')

for i in range(10000):
    x = heart(i) * 20
    y = show(i) * 20
    goto(x, y)
    for j in range(5):
        color('#f73487')
        goto(x,0)
done()