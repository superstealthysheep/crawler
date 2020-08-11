def owoify(input_string):
    vowels = ["a", "e", "i", "o", "u"]
    output_string = ""
    for letter in input_string:
        if letter in vowels:
            output_string += (letter + "w" + letter)
        else:
            output_string += letter
    return(output_string)

#print(owoify("hello there"))
