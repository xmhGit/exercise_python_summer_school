# from sys import argv
# script,filename = argv
filename = raw_input("Input the filename of your text:\n")
content = open(filename)
print("The content of %s:" % filename)
print content.read()  # 
