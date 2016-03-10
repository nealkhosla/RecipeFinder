from easygui import *
import lookup
import diet
import pickle
import string
import tagged_truths
import unicodedata
from collections import defaultdict


def calculate_precision_and_recall():
	guesses = defaultdict(set)
	all_diets = [diets[diet] for diet in diets]
	num_items = 0
	for recipe in recipes:
		if recipe in tagged_truths.truths:
			num_items += 1
			(name, ingredients, url) = recipes[recipe]
			for ingredient in ingredients:
				ingredient = unicodedata.normalize('NFC', ingredient).encode('ascii','ignore')
				exclude = set(string.punctuation)
				ingredient = ''.join(ch for ch in ingredient if ch not in exclude)
				for word in ingredient.split():
					for food in lookup.foods:
						# If this food is a subtring of the word
						if word.lower().find(food) != -1:
							# Find the class
							ingredient_class = lookup.foods.get(food)
							# Check if it's a restriction
							for diet in all_diets:
								for restriction in diet.getClassDisallowedList():
									if issubclass(ingredient_class, restriction):
										guesses[recipe].add(diet)
		if num_items == len(tagged_truths.truths):
			break

	true_positives = 0.0
	positives = 0.0
	false_negatives = 0.0
	for guess in guesses:
		allowed_diets = set(all_diets) - guesses[guess]
		print str(guess) + " guessed allowed diets: " + str(allowed_diets)
		print str(guess) + " allowed diets: " + str(tagged_truths.truths[guess])
		print str(guess) + " true positives: " + str(allowed_diets & set(tagged_truths.truths[guess]))
		true_positives += len(allowed_diets & set(tagged_truths.truths[guess]))
		positives += len(allowed_diets)
		false_negatives += len(set(tagged_truths.truths[guess]) - allowed_diets)
		# print str(guess) + ": " + str(guesses[guess])
	print "precision: " + str(true_positives / positives)
	print "recall: " + str(true_positives / (true_positives + false_negatives))

def suggest_recipes(restrictions, search_term, diet, n=10):
	results = []
	for recipe in recipes:
		to_add = True
		found = False
		if len(results) == n:
			break
		(name, ingredients, url) = recipes[recipe]
		for ingredient in ingredients:
			ingredient = unicodedata.normalize('NFC', ingredient).encode('ascii','ignore')
			exclude = set(string.punctuation)
			ingredient = ''.join(ch for ch in ingredient if ch not in exclude)
			if ingredient.find(search_term) != -1:
				found = True
			for word in ingredient.split():
				for food in lookup.foods:
					# If this food is a subtring of the word
					if word.lower().find(food) != -1:
						# Find the class
						ingredient_class = lookup.foods.get(food)
						# Check if it's a restriction
						for restriction in restrictions:
							if issubclass(ingredient_class, restriction):
								to_add = False
		if to_add and found:
			results.append(recipes[recipe])

	print choice + ": " + str(len(results))
	for result in results:
		print result[0]
		print result[1]
		print "\n\n\n"


diets = {"Vegan":diet.VeganDiet,
"Lacto vegetarian":diet.LactoDiet,
"Lacto-ovo vegeterian":diet.LactoOvoDiet,
"Lactose Intolerant":diet.LactoseIntolDiet,
"Pescatarian":diet.PescatarianDiet,
"Nonvegetarian":diet.NonVegetarianDiet,
"Gluten Free":diet.GlutenFreeDiet}

recipes = pickle.load(open("recipes.p", "rb"))

msg ="What diet do you subscribe to?"
title = "Recipe Search"
choices = [diet for diet in diets]
choice = choicebox(msg, title, choices)

search_msg = "You selected a " + str(choice) + " diet. Now enter an ingredient to search for or leave blank to search for all recipes"
search_term = enterbox(search_msg, "Recipe Search")

diet = diets[choice]
restrictions = diet.getClassDisallowedList()

suggest_recipes(restrictions, search_term, diet)
