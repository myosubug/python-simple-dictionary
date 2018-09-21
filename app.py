import json
data = json.load(open("data.json"))

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doens't exist in the dictionary, please check your word again"

word = input("Enter word: ")
print(dictionary(word))