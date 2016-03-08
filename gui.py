from easygui import *
import lookup
import diet
import pickle
import unicodedata

diets = {"Vegan":diet.VeganDiet,
"Lacto vegetarian":diet.LactoDiet,
"Lacto-ovo vegeterian":diet.LactoOvoDiet,
"Fruitarian":diet.FruitarianDiet,
"Lactose Intolerant":diet.LactoseIntolDiet,
"Pescatarian":diet.PescatarianDiet,
"Nonvegetarian":diet.NonVegetarianDiet,
"Gluten Free":diet.GlutenFreeDiet}

recipes = pickle.load(open("recipes.p", "rb"))

msg ="What diet do you subscribe to?	"
title = "Recipe Search"
choices = ["Vegan", "Lacto vegetarian", "Lacto-ovo vegeterian", "Fruitarian", "Lactose Intolerant", "Pescatarian", "Nonvegetarian", "Gluten Free"]
choice = choicebox(msg, title, choices)

search_msg = "You selected a " + str(choice) + " diet. Now enter an ingredient to search for or leave blank to search for all recipes"
search_term = enterbox(search_msg, "Recipe Search")

diet = diets[choice]

restrictions = diet.getClassDisallowedList()
results = []
for recipe in recipes:
	to_add = True
	found = False
	if len(results) == 10:
		break
	(name, ingredients, url) = recipes[recipe]
	for ingredient in ingredients:
		ingredient = unicodedata.normalize('NFC', ingredient).encode('ascii','ignore')
		if ingredient.find(search_term) != -1:
			found = True
		for word in ingredient.split():
			# TODO: Strip punctuation
			ingredient_class = lookup.foods.get(word.lower())
			if ingredient_class:
				for restriction in restrictions:
					if issubclass(ingredient_class, restriction):
						to_add = False
	if to_add and found:
		results.append(recipes[recipe])

print len(results)
for result in results:
	print result[0]
	print result[1]
	print "\n\n\n"