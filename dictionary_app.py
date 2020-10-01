import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translator(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s instead? if yes enter Y or N if no." % get_close_matches(word,data.keys())[0]).upper()
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't match, please double chack it."
        else:
            return "We didn't understsand your entry word."
    else:
        return "The word doesn't match, please double chack it."

word = input("Enter word: ")
Definition = translator(word)
if type(Definition) == list:
    for x in Definition:
        print(x)
else:
    print(Definition)