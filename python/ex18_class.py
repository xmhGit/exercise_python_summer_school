# To create instance using :
# apple = mc.fruit()
# apple.peel()
# call the function of peel()
# apple.edible
class fruit(object):
    def __init__(self):
        self.edible = True
    	self.cook = False
    def peel(self):
    	print "Peel me."

