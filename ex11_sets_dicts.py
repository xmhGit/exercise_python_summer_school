# -*- coding: UTF-8 -*- 
my_set = {1,2,3,'Xu',(1,2)} 
# a = {{1,2},[1,2]}
# TypeError: unhashable type: 'set'
# TypeError: unhashable type: 'list'
# 这句话的意思是说：list、set不能作为set的元素。
my_dict = {1:1,(1,2):2,"H":3}
# TypeError: unhashable type: 'list'
# 不能更改的序列不能作为另外序列的元素？
print my_set
print my_dict
print my_dict[1]

