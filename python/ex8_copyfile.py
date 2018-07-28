# -*- coding: UTF-8 -*-
# 加入头，即可识别中文
from sys import argv
script,myfile,copyfile = argv
content = open(myfile,'r')
content_copy = open(copyfile,'w+')

text = content.read()
content_copy.write(text)

content.seek(0,0)  # 重新设置文件读取指针到开头
print("The front one is :")
print(content.read())
content_copy.seek(0,0)
print "The later one is :\n",content_copy.read()  # print here can't use () 

content_copy.close()
content.close()

