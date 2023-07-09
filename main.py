# Data Types
# String
firstName = input("What is your First Name?\n")
print("The initial of your first name is " + firstName[0]) # Substrings locate a letter in the string based on the value given for example "Callum" with a substring of [0] would output C
print("The last letter of your name is " + firstName[len(firstName) - 1]) # Substrings don't have to be exact numbers, the numbers can be determined by functions, like len()
# Substrings count from 0 

# Printing Types
print(firstName + " is a " + str(type(firstName)))

# Integer
print("123" + "456") # Strings are determined using "", the output of this code will be 123456
print(123 + 456) # Integers do not need "", integers are only whole numbers, the output of this code would be 579

# Float
pi = 3.14159 # Floats are initialized like integers, except Floats must contain a point -> . <- somewhere in the number
print(str(pi) + " is a " + str(type(pi)))

# Boolean
earthRound = True # Booleans come in two states, True or False
earthFlat = False
print("Is the Earth Round? " +str(earthRound) + "\nIs the Earth Flat? " + str(earthFlat))