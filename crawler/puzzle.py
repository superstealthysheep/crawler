import random
from datetime import datetime
import owoifier

"""Puzzle category ideas:
    German vocab genders
    Musical interval ID
    Evaluating algebraic expressions
    Countries and capitals
    --De-owoifying phrases randomly picked from Jane Eyre or something
"""

#class Puzzle:
def alg_puzzle(): #should return an attack multiplier given how well you do. I'll start with just some algebraic thing.
    #format 1: "(int1 * int2) + int3"
    int_list = []
    format = "({} * {}) + {}" #could potentially eventually make a list of these formats

    for i in range(0, 3): #future: make the number of ints generated match the format or find a way to throw out extras
        int_list.append(random.randrange(0, 13))

    prompt = format.format(*int_list) #woah, this * thing is cool. I learned something today.
    ans = eval(prompt)  #!!!!!!!!!!!!!!EVAL IS SKETCHY I THINK SO FIND A BETTER WAY TO PARSE THIS SOMETIME PLEASE

    start_time = datetime.now()
    response = input(prompt + " = ")
    response_time = (datetime.now() - start_time).total_seconds() #future: make this into a function to avoid repetition

    print("ans: {}, response: {}".format(ans, response))
    if response == str(ans): #I choose to cast ans as a string as opposed to casting response as an int in order to avoid errors
        print("Nice job!")
        return (4 / response_time) #tweak this constant for it to fit
    else:
        return 0

def owo_puzzle():
    source_string = "Python is an object-orientated language"
    prompt = owoifier.owoify(source_string)

    start_time = datetime.now()
    response = input(prompt +"\n> ")
    response_time = (datetime.now() - start_time).total_seconds() #future: make this into a function to avoid repetition

    if response.upper() == source_string.upper():
        print("Nice job!")
        return (len(source_string) / response_time * 2/3)


#puzzle = Puzzle()
#print(alg_puzzle())
#print(owo_puzzle())
