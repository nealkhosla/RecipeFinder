from easygui import *

msg ="What diet do you subscribe to?	"
title = "Recipe Search"
choices = ["Vegan", "Lacto vegetarian", "Lacto-ovo vegeterian", "Fruitarian", "Lactose Intolerant", "Pescatarian", "Nonvegetarian", "Gluten Free"]
choice = choicebox(msg, title, choices)

search_msg = "You selected a " + str(choice) + " diet. Now enter an ingredient to search for or leave blank to search for all recipes"
search_term = enterbox(search_msg, "Recipe Search")