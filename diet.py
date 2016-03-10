# Defines the Diet ontology.  Provides structure for inheriting
# list of disallowed food groups.  
import ingredient





class Diet(object):

	# init the name and instance's disallowedList
	def __init__(self, name, instanceDisallowedList=[]):
		self.name = name
		self.instanceDisallowedList = instanceDisallowedList

	# gets the class' disallowed list
	@staticmethod
	def getClassDisallowedList():
		return []

	# gets the class' disallowed list + instance's disallowed list
	def getFullDisallowedList(self):
		return self.instanceDisallowedList + Diet.getClassDisallowedList()


# Diet subclasses
class VegetarianDiet(Diet):
	@staticmethod
	def getClassDisallowedList():
		return [ingredient.Meat] + Diet.getClassDisallowedList()

	def getFullDisallowedList(self):
		return self.instanceDisallowedList + VegetarianDiet.getClassDisallowedList()

class NonVegetarianDiet(Diet):
	@staticmethod
	def getClassDisallowedList():
		return [] + Diet.getClassDisallowedList()

	def getFullDisallowedList(self):
		return self.instanceDisallowedList + NonVegetarianDiet.getClassDisallowedList()


# VegetarianDiet subclasses
class VeganDiet(VegetarianDiet):
	@staticmethod
	def getClassDisallowedList():
		return [ingredient.Lacto, ingredient.Ovo] + VegetarianDiet.getClassDisallowedList()

	def getFullDisallowedList(self):
		return self.instanceDisallowedList + VeganDiet.getClassDisallowedList()

class LactoDiet(VegetarianDiet):
	@staticmethod
	def getClassDisallowedList():
		return [ingredient.Ovo] + VegetarianDiet.getClassDisallowedList()

	def getFullDisallowedList(self):
		return self.instanceDisallowedList + LactoDiet.getClassDisallowedList()

class LactoOvoDiet(VegetarianDiet):
	@staticmethod
	def getClassDisallowedList():
		return [] + VegetarianDiet.getClassDisallowedList()

	def getFullDisallowedList(self):
		return self.instanceDisallowedList + LactoOvoDiet.getClassDisallowedList()

# NonVegetarianDiet subclasses
class LactoseIntolDiet(NonVegetarianDiet):
	@staticmethod
	def getClassDisallowedList():
		return [ingredient.Lacto] + NonVegetarianDiet.getClassDisallowedList()

	def getFullDisallowedList(self):
		return self.instanceDisallowedList + LactoIntolDiet.getClassDisallowedList()

class PescatarianDiet(NonVegetarianDiet):
	@staticmethod
	def getClassDisallowedList():
		return [ingredient.RedMeat, ingredient.Poultry] + NonVegetarianDiet.getClassDisallowedList()

	def getFullDisallowedList(self):
		return self.instanceDisallowedList + PescatarianDiet.getClassDisallowedList()

class GlutenFreeDiet(NonVegetarianDiet):
	@staticmethod
	def getClassDisallowedList():
		return [ingredient.Grain] + NonVegetarianDiet.getClassDisallowedList()

	def getFullDisallowedList(self):
		return self.instanceDisallowedList + GlutenFreeDiet.getClassDisallowedList()

glFreeVegeDiet = GlutenFreeDiet("veganD", [ingredient.Meat])

# print glFreeVegeDiet.getClassDisallowedList()
# print glFreeVegeDiet.getFullDisallowedList()

