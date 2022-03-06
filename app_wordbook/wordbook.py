#!/usr/bin/python3
import json
from difflib import get_close_matches

elements = json.load(open("wordbook.json"))

def findmeaning(word):
    if word.lower() in elements:	
        return elements[word.lower()]
    elif word.upper() in elements:
        return elements[word.upper()]
    elif word.title() in elements:
        return elements[word.title()]
    elif len(get_close_matches(word, elements.keys())) > 0:
        closematches = (get_close_matches(word, elements.keys())[0])
        user_decision = input("Did you mean %s ? [y/n] " % closematches )

        if user_decision == "y":
            return elements[get_close_matches(word, elements.keys())[0]]
        elif user_decision == "n":
            return "I cannot find your word, I'm sorry."
        else:
            return "Something went wrong, try again another time."

    else:
        return "I can't find this word. Please look for spelling mistakes."

word = input("Type Any Word Here: ")

output = findmeaning(word)

if type (output) == list:
    for item in output:
        print(item)
else:
    print(output)

