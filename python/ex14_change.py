from numpy import *
myindex = array(range(10,21,1))/10.0
print myindex
for i in range(len(myindex)):
    print myindex[i]**myindex[i]

