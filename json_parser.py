import sys
from json import loads
import cPickle as pickle
import math


"""
Returns true if a file ends in .json
"""
def is_json(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parse_json(json_file):
    with open(json_file, 'r') as f:
        # key: id
        # value: (name, ingredients, url)
        recipes = {}
        palindrome_count = 0
        empty_count = 0
        
        for line in f:
            json_line = loads(line)
            recipe_id = json_line['_id']['$oid']
            name = json_line['name']
            ingredients = json_line['ingredients'].split('\n')

            # check for empty list of ingredients
            # check for palindromes in ingredients
            skip = False
            total_length = 0
            for ingr_str in ingredients:
                total_length += len(ingr_str)

                front_half = ingr_str[:len(ingr_str) // 2]
                back_half = ingr_str[int(math.ceil(len(ingr_str) / 2)) + 1:]

                if front_half == back_half:
                    skip = True
            if total_length == 0:
                empty_count += 1
                continue
            if skip:
                palindrome_count += 1
                continue

            url = json_line['url']

            recipes[recipe_id] = (name, ingredients, url)

        pickle.dump(recipes,open("recipes.p", "wb"))
        print "palindrome count: ", palindrome_count
        print "empty_count: ", empty_count
        #recipes = pickle.load(open("recipes.p", "rb"))
            

# def createDatFile(fileName, entries):
#     f = open(fileName, 'a+')
#     for entry in entries:
#         f.write('|'.join(entry) + '\n')



"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if is_json(f):
            parse_json(f)
            print "Success parsing " + f

if __name__ == '__main__':
    main(sys.argv)
