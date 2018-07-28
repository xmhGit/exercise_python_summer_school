# -*- conding: UTF-8 -*-
from sys import argv
from numpy import pi


def func_minu(a,b):
    a = float(a)
    b = float(b)
    c_a = 2*pi*a*10**3
    c_b = 2*pi*b*10**3
    return abs(c_a - c_b)


r_earth = 6000  # km
r_mar = 3000 
script,r_planet = argv
if (func_minu(r_earth,r_planet) < func_minu(r_mar,r_planet)):
    print "The planet is closer to the Earth"
elif (func_minu(r_earth,r_planet) > func_minu(r_mar,r_planet)):
    print "The planet is closer to the Mars"
else:
    print "The planet isn't closer to any of the planets"
# 尽量不要比较两个浮点数的大小，因为系统的表示总会有误差。
