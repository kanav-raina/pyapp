import json
from difflib import get_close_matches

data=json.load(open("data.json"))


def translate(w):
    w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean {0} instead?\nenter y if yes or n if no".format(get_close_matches(w,data.keys())[0]))
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="n":
            return "the word does'nt exist"
        else:
            return "we didnot understand your entry"
    else:
        return ("word doesn't exist")
word=str(input("enter word"))
output=translate(word)
if type(output)==list:
    for item in output:
        print (item)
else:
    print(output)






































