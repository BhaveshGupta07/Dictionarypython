import json
from difflib import get_close_matches
data= json.load(open("data.json"))

def translate(x):  #translate function
    x=x.lower()  #returns lowercase 
    if x in data:  #check for lowercase keys in data 
        return data[x]
    elif x.title() in data: #check first letter of data keys in capital
        return data[x.title()]
    elif x.upper() in data:
        return data[x.upper()] #check for uppercase keys in data 
    elif len(get_close_matches(x, data.keys())) > 0: #chek if the closematched word exist in the data keys or not 
        print("did you mean by %s"%get_close_matches(x, data.keys())[0]) #it will print the key with close match exist at first [0,1,2,3,4,5,6,7,8,9]
        decide=input("if yes then enter y or n= ")
        if decide == "y":
            return data[get_close_matches(x, data.keys())[0]]
        elif decide == "n":
            return print(" you have entered wrong input ")
        else:
            print("data not found in the dictionary")
    else:
        print("data not found in the dictionary")


x=input("enter the word to find in dictionary = ")
out=translate(x)

if type(out) == list:
    for i in out:
         print(i)
else:
    print(out)



