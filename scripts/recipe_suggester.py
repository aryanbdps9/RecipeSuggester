import os
from os import path
import utils

dumpdir = path.join('..', 'dumps')

try:
    data = utils.load(path.join(dumpdir, 'datadict.pkl'))
    ingredient_dict = utils.load(path.join(dumpdir, 'ingredient_dictionary.pkl'))
except Exception as e:
    print("pkl files not found. Please run 'ingredient_dictionary.py' first. Exiting...")
    exit(1)

def ranker(input_ingredients):
    def printer(*args):
        print("ranker: ", end="")
        print(*args)
    unigrams = set(input_ingredients)
    candidates  = [(ingredient_dict[uni], len(ingredient_dict[uni])) for uni in unigrams if uni in ingredient_dict]
    candidate_scores = {}
    for candidate_list, score in candidates:
        for candidate in candidate_list:
            if candidate not in candidate_scores:
                candidate_scores[candidate] = 0.0
            candidate_scores[candidate] += 1.0/score
    
    scored_ids = sorted(candidate_scores, key=lambda x: candidate_scores[x], reverse=True)
    return scored_ids

# take list of ingredients from user
# find the list of recipes which satisfy these requirements
# display them

def give_dish(h):
    #h = input("Enter comma separated items and then press enter. Press ctrl+C then <enter> to exit.\n").strip()
    l=h.strip()
    input_ingredients = [item.strip().lower() for item in l.split(",")]
    ranked_recipes = ranker(input_ingredients)
    titles=[]
    receipes=[]
    for idx, ranked_recipe in enumerate(ranked_recipes):
        receipes.append(data[ranked_recipe])
        titles.append(ranked_recipe+'\t'+data[ranked_recipe]['title'])
        if (idx > 20):
            break
    return titles,receipes
    
