import Entity
from Entity import Entity

class Animate(Entity):
	maxHealth = 1
	health = 1
	strength = 1
	stealth = 1
	
	equipped = {"hand":None, "body":None}
	attributes = {}

	def __init__():
		pass
	'''
		This class doesn't need an initializer, it only exists to
		be a parent class
	'''
