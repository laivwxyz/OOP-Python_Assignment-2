# Dela Cruz, Lailanie E. _ BSCPE 1-4
# Assignment 2
# Problem 2 - Decryption

import pyfiglet

# Designing the assignment 2, problem number 2
assignment_number = pyfiglet.figlet_format('Assignment 2', font = 'digital')
problem_number = pyfiglet.figlet_format('Problem 2', font = 'digital')
problem_title = pyfiglet.figlet_format('Decryption', font = 'digital')
print('\033[93m' + assignment_number)
print('\033[93m' + problem_number)
print('\033[93m' + problem_title)

# Ask the user to input an encrypted text
input_str = input("\033[92m" + "Enter a string to decrypt: ")
output_str = "\033[92m"
# Check every character
for i in range (len(input_str)):
# if *, change to a
    if input_str[i] == "*":
        output_str += "a"
# if &, change to e
    elif input_str[i] == "&":
        output_str += "e"
# if #, change to i
    elif input_str[i] == "#":
        output_str += "i"
# if +, change to o
    elif input_str[i] == "+":
        output_str += "o"
# if !, change to u
    elif input_str[i] == "!":
        output_str += "u"
    else:
        output_str += input_str[i]

# print the output
print(output_str)