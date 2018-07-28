#-*- coding: UTF-8 -*-
# 采用compose的方法或许优于多重继承的方法
def parent(object):
	def __init__(self):
		self.role = "parent"


def child(object):  # 均直接继承自object
	def __init__(self):
		self.role = "child"

