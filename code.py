import json
import difflib

#This returns word meaning for exact match
def translate(word):
    return data[word]

#User input
def user_input():
    get_data=input("Enter the word to search for meaning : ")
    get_data=get_data.lower()
    return get_data

#Loading the json file 
fp=open('data.json','r')
data=json.load(fp)

#Let's keep a track of all the keys 
l=list(data.keys())

get_data=user_input()

#Checking if the exact word exists and if does return meaning
if get_data in l:
    print(''.join(translate(get_data)))

else:
    #First check if user entered extra word or mispelled by mistake by checking closeness
    max=0.0 #max ratio value
    word=""  #max close word
    for each in l:
        x=difflib.SequenceMatcher(None,get_data,each).ratio()
        if(x>max):
            max=x
            word=each
        else:
            continue
    
    #Now check if mistake was done if closeness is >8.0
    if(max>=.75 and word!=''):
        #Prompt user for autocorrection
        print("Did you mean "+word+ " ?  yes or no")
        get_prompt=input().lower()
        if(get_prompt=='yes'):
            print(''.join(translate(word)))
        
        #User refused auto-correct
        else:
            print("The word does not exist.  Please double-check it.")
        
    #No match not even suggestion
    else :       
        print("The word does not exist.  Please double-check it.")