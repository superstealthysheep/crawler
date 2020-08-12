def owoify(input_string):
    vowels = ["a", "e", "i", "o", "u"]
    output_string = ""
    for letter in input_string:
        if letter.lower() in vowels:
            if letter == letter.upper():
                output_string += (letter + "w" + letter.lower()) #So O --> Owo, not OwO or owo
            else:
                output_string += (letter + "w" + letter) #normal case
        else:
            output_string += letter
    return(output_string)

#print(owoify("hello there"))
