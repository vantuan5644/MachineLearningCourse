# Bartender Project - Basic Python


"""
Given two above dictionaries, construct the Python program (using functions) to ask users entering their
tastes and then match randomly with the ingredients (print out outputs for user).
"""

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

import random


def print_ingredients():
    def get_answer(answer=""):
        while answer not in questions.keys():
            key = random.choice(list(questions.keys()))
            start_index = questions[key].index("ye")
            statement = questions[key][start_index:-1]
            print(f"Input \"{key}\" if {statement}, otherwise just press Enter")
            answer = input()
        return answer

    answer = get_answer()
    ingredients_list = ingredients[answer]
    print(f"Here's what you need for the {answer} drink:", " + ".join(ingredients_list))


print_ingredients()
