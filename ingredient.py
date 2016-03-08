class Ingredient(object):
	def __init__(self):
		self.name = "Ingredient"

# Ingredient Subclasses
class Grain(Ingredient):
	def __init__(self):
		self.name = "Grain"

class Lacto(Ingredient):
	def __init__(self):
		self.name = "Lacto"

class Ovo(Ingredient):
	def __init__(self):
		self.name = "Ovo"

class Meat(Ingredient):
	def __init__(self):
		self.name = "Meat"

class Vegetable(Ingredient):
	def __init__(self):
		self.name = "Vegetable"

class Fruit(Ingredient):
	def __init__(self):
		self.name = "Fruit"

# Meat Subclasses
class Poultry(Meat):
	def __init__(self):
		self.name = "Poultry"

class RedMeat(Meat):
	def __init__(self):
		self.name = "RedMeat"

class Seafood(Meat):
	def __init__(self):
		self.name = "Grain"


# Poultry Subclasses
class Duck(Poultry):
	def __init__(self):
		self.name = "Duck"

class Chicken(Poultry):
	def __init__(self):
		self.name = "Chicken"

class Turkey(Poultry):
	def __init__(self):
		self.name = "Turkey"


# RedMeat Subclasses
class Beef(RedMeat):
	def __init__(self):
		self.name = "Beef"

class Pork(RedMeat):
	def __init__(self):
		self.name = "Pork"

class Lamb(RedMeat):
	def __init__(self):
		self.name = "Lamb"

class Veal(RedMeat):
	def __init__(self):
		self.name = "Veal"

# Seafood Subclasses
class Fish(Seafood):
	def __init__(self):
		self.name = "Fish"

class Shellfish(Seafood):
	def __init__(self):
		self.name = "Shellfish"

# Fish Subclasses
class Anchovy(Fish):
	def __init__(self):
		self.name = "Anchovy"

class Bass(Fish):
	def __init__(self):
		self.name = "Bass"

class Cod(Fish):
	def __init__(self):
		self.name = "Cod"

class Halibut(Fish):
	def __init__(self):
		self.name = "Halibut"

class MahiMahi(Fish):
	def __init__(self):
		self.name = "MahiMahi"

class Salmon(Fish):
	def __init__(self):
		self.name = "Salmon"

class Sardine(Fish):
	def __init__(self):
		self.name = "Sardine"

class Snapper(Fish):
	def __init__(self):
		self.name = "Snapper"

class Trout(Fish):
	def __init__(self):
		self.name = "Trout"

class Tuna(Fish):
	def __init__(self):
		self.name = "Tuna"

# Shellfish Subclasses
class Mollusc(Shellfish):
	def __init__(self):
		self.name = "Molluscs"

class Crustacean(Shellfish):
	def __init__(self):
		self.name = "Crutaceans"

# Mollusc Subclasses
class Mussel(Mollusc):
	def __init__(self):
		self.name = "Mussel"

class Clam(Mollusc):
	def __init__(self):
		self.name = "Clam"

class Octopus(Mollusc):
	def __init__(self):
		self.name = "Octopus"

class Oyster(Mollusc):
	def __init__(self):
		self.name = "Oyster"

class Scallop(Mollusc):
	def __init__(self):
		self.name = "Scallop"

class Squid(Mollusc):
	def __init__(self):
		self.name = "Squid"

# Crustacean Subclasses
class Crab(Crustacean):
	def __init__(self):
		self.name = "Crab"

class Lobster(Crustacean):
	def __init__(self):
		self.name = "Lobster"

class Shrimp(Crustacean):
	def __init__(self):
		self.name = "Shrimp"
