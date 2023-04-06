# Dela cruz, Lailanie E. _ BSCPE 1-4
# Assignment 2
# Problem 3 - The Vigenere Cipher

import pyfiglet

# Designing the assignment 2, problem number 3
assignment_number = pyfiglet.figlet_format('Assignment 2', font = 'digital')
problem_number = pyfiglet.figlet_format('Problem 3', font = 'digital')
problem_title = pyfiglet.figlet_format('The Vigenere Cipher', font = 'digital')
print('\033[93m' + assignment_number)
print('\033[93m' + problem_number)
print('\033[93m' + problem_title)

# Function generates key in a continuous process until it's length isn't equal to the length of original text
def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

# With the help of the key, the function returns the encrypted text generated
def cipher_text(message, key):
    cipher_text = []
    for i in range(len(message)):
        x = (ord(message[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

# Use the decryption function to decrypt the encrypted text and returns the original text
def original_text(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

# FUnction asks the user for the plaintext and print out the output of the program 
if __name__ == "__main__":
    message = input('\033[34m' + "Message(all uppercase & no spaces): ")
    keyword = input('\033[34m' +"Keyword(all uppercase & no spaces): ")
    key = generate_key(message, keyword)
    cipher_text = cipher_text(message, key)
    print('\033[34m' + "Ciphertext: ", cipher_text)