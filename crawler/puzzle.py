import random
from datetime import datetime

"""Puzzle category ideas:
    German vocab genders
    Musical interval ID
    Evaluating algebraic expressions
    Countries and capitals
    De-owoifying phrases randomly picked from Jane Eyre or something
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
    response_time = (datetime.now() - start_time).total_seconds()

    print("ans: {}, response: {}".format(ans, response))
    if response == str(ans): #I choose to turn ans to a string as opposed to turning response to an int in order to avoid errors
        return (4 / response_time) #tweak this constant for it to fit
    else:
        return 0



#puzzle = Puzzle()
#print(alg_puzzle())
