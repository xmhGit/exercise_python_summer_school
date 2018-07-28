import numpy as np
from sys import argv


def cal_cir(r):
	cir = 2*np.pi*r*10**3
	return cir
# script,r = argv
# r = float(r)  # argv's method also input the type of string
# pi=3.14  # constant pi
# r=6378  # the radius of the earth's equator, unit: km\
# r = float(raw_input("Input the radius of the earth(unit:km):\n"))  
    # force to invert the string to float 
    # when using raw_input() and argv simultaneously, it also can work. But the 
    # second raw_input() will replace the first argv.
# c=2*pi*r*10**3  # consistence of the earth's equator
# c_p=2*np.pi*r*10**3  # another method to get pi
earth_r = float(raw_input("Input the radius of the Earth(unit:km):\n"))
earth_cir = cal_cir(earth_r)
print "The circumference of the earth's equator is %r." % earth_cir
Mar_r = float(raw_input("Input the radius of the Martian(unit:km):\n"))
Mar_cir = cal_cir(Mar_r)
print "The circumference of the Mar's equator is %r." % Mar_cir
# surface_area = 4*np.pi*r**2*10**6  # unit:m**2
# print("Earth Information:")
# print("The circumference of the earth's equator is %.1f m" % c)
# print("\tThe circumference of the earth's equator is\n\t  %.3f m" % c_p)
# print("\tThe surface area of the earth is\n\t  %.3f m^2" % surface_area)

# print "\n"
# print 7/4
# print 7/4.0 

