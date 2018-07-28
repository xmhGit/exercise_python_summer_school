import numpy as np
from sys import argv
# calculate area
script,length = argv
length = float(length)
width = float(raw_input("Input the width:\n"))
area = length*width
print("The area is : %.3f" % area)
