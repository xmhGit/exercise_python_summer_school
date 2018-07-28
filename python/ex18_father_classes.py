# -*- coding: UTF-8 -*-
class organism(object):
	def __init__(self):  # 性质
		self.life = "live"
		self.power = "magic"

class animal(organism):
	def __init__(self):
		super(animal,self).__init__()
		self.position = "move"
		self.varity = "billions"

class vertebrate(animal):
	def __init__(self):
		super(vertebrate,self).__init__()
		self.vertebrate = True

class mammal(vertebrate):
	def __init__(self):
		super(mammal,self).__init__()
		self.Mammary_gland = True

class dog(mammal):
	def __init__(self):
		super(dog,self).__init__()
		dog.lifetime = "10 years" 
