a = {1,2,3}
e = {1:'a',2:'b',3:'c'}
for i in a:
    print i
for i in a:
    print e[i]
print len(a)
#for i in range(len(a)):
#    print a[i]
# TypeError: 'set' object does not support indexing

