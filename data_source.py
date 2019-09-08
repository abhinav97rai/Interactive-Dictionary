import json
from difflib import get_close_matches
data=json.load(open("data.json")) #list(dictionary) of word

Sample_Word=input("Enter the word: ") #word that user wants to search
Sample_Word=Sample_Word.lower()
Wrong_Sample="entered word is incorrect" #message to be displayed in case entered word is wrong

def word_search(Sample_Word): #function to search the meaning of inputed word
    if Sample_Word in data:
        return data[Sample_Word]
    elif len(get_close_matches(Sample_Word,data.keys()))>0:  #in the case of close match 
        ans=input("Did you mean %s instead :" % get_close_matches(Sample_Word,data.keys())[0])
        if ans=='y' or ans=='Y':
            return data[get_close_matches(Sample_Word,data.keys())[0]]
        elif ans=='n' or ans=='N':
            return "your word not found"
        else:
            return "we didn't understand your awnser"
    else:
        return Wrong_Sample #in case entered word is wrong


#to optimixe the output
output=word_search(Sample_Word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
