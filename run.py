"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = ("This morning {name} woke up feeling {word_one}. 'It is going to be a {word_two} day!' Outside, a bunch of {animal}s were protesting to keep {food} in stores. They began to {verb_one} to the rhythm of the {noun_one}, which made all the {fruit}s very {word_three}. Concerned, {name} texted {superhero}, who flew {name} to {country} and dropped {name} in a puddle of frozen {dessert}. {name} woke up in the year {year}, in a world where {noun_two}s ruled the world.")

print("Mad libs has started")
name = input("Enter a name: ")
word_one = input("{name}, Enter your first adjective: ").format(name=name)
word_two = input("Enter your second adjective: ")
word_three = input("Enter your third adjective: ")
verb_one = input("Enter a verb: ")
noun_one = input("Enter a noun: ")
noun_two = input("Enter a second noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a desset: ")
year = input("Enter a year: ")

print(STORY.format(name=name, word_one=word_one, word_two=word_two, animal=animal, food=food, verb_one=verb_one, noun_one=noun_one, fruit=fruit, word_three=word_three, superhero=superhero, country=country, dessert=dessert, year=year, noun_two=noun_two))










