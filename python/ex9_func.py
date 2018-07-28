# -*- coding: UTF-8 -*-


def print_none():  # : is essential
    print "Hello World."
    

def print_one(arg):
    print "I like %s." % arg
    

def print_two(arg1,arg2):
    print "I like %s and %s." % (arg1,arg2)
    
    
print_none()
print_one("apple")
print_two("apple","banana")
