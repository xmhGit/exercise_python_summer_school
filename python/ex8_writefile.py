from sys import argv
script,filename = argv
content = open(filename,'w+')  # r:read only w;a;w+;a+
			                   # w+:write and read
line1 = "My name is Xu Minghui"
line2 = "I repeated it just now"

content.write(line1)
content.write("\n")
content.write(line2)
content.write("\n")

content.seek(0,0)  # move to the front of content, otherwise, we can't read it
print content.read()

content.close()

