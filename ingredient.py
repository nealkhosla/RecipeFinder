class Ingredient:
	def __init__(self, name="Ingredient", keywords=[]):
		self.name = name
		self.keywords = keyword


class Grain(Ingredient):
	def __init__(self, name="Grain", keywords=[]):
		super(Grain, self).__init__(name, keywords)

class Lacto(Ingredient):
	def __init__(self, name="Lacto", keywords=[]):
		super(Lacto, self).__init__(name, keywords)

class Ovo(Ingredient):
	def __init__(self, name="Ovo", keywords=[]):
		super(Ovo, self).__init__(name, keywords)

class Meat(Ingredient):
	def __init__(self, name="Meat", keywords=[]):
		super(Meat, self).__init__(name, keywords)

class Vegetable(Ingredient):
	def __init__(self, name="Vegetable", keywords=[]):
		super(Vegetable, self).__init__(name, keywords)

class Fruit(Ingredient):
	def __init__(self, name="Fruit", keywords=[]):
		super(Fruit, self).__init__(name, keywords)

class Poultry(Meat):
	def __init__(self, name="Poultry", keywords=[]):
		super(Poultry, self).__init__(name, keywords)

class RedMeat(Meat):
	def __init__(self, name="RedMeat", keywords=[]):
		super(RedMeat, self).__init__(name, keywords)

class Seafood(Meat):
	def __init__(self, name="Seafood", keywords=[]):
		super(Seafood, self).__init__(name, keywords)