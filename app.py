import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())):
        yn = input("did you mean '%s'? Enter Y/y if yes, N/n if no.\n" % get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn =="y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "There is no such word :(, please check your word again!"
    else:
        return "The word doens't exist in the dictionary, please check your word again"

word = input("Enter word: ")
output = dictionary(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)