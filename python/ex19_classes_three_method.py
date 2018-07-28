# -*- coding: UTF-8 -*-
# 此程序用于说明三种继承方式
class parent(object):
	def __init__(self):
		self.role = "members of family"
		self.experience = "abundant"
		self.love_to_kid = True
	def Tokid(self):
		print "I love you, my kid."
#class child(parent): # No.1:implicit inheritance
#	pass  # result in follow:
# child = child()
# >>> child.role
# 'parent'
# >>> child.experience
# 'abundant'
# >>> child.Tokid()
# I love you, my kid.

#class child(parent):  # No.2:Explicitly override
#	def __init__(self):
#		super(child,self).__init__()
#		self.role = "child"
#		self.experience = "little"
#		self.love_to_parent = True
#	def Toparent(self):
#		print "I love you, my parent."
#	def Tokid(self):
#		print "Just do it!"
# >>> child.role
# 'child'
# >>> child.Toparent()
# I love you, my parent.
# >>> child.experience
# 'little'
# >>> child.Tokid()
# Just do it!

class child(parent):  # No.3:Alter between the two version
    def __init__(self):
        super(child,self).__init__()
        self.role = "child"
        self.experience = "little"
        self.love_to_parent = True
    def Toparent(self):
        print "I love you, my parent."
    def Tokid(self):
        print "Just do it!"
#	super(child,self).altered()  这句话没有实现
