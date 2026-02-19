import string, sys, operator
from pathlib import Path
from collections import Counter
from prettytable import PrettyTable

def main():

        ### VALIDATE PROGRAM USAGE AND FILE PATH ###

    # Check for valid program usage
    if len(sys.argv) != 2:
        print("Usage: myscript.py <filename>")
        return
    
    ## Import and read filename for analysis
    filename = str(sys.argv[1])
    cwd = Path().resolve() 
    filepath = cwd.joinpath(filename)   

    ## Check if the path for the provided filename exists in the current directory
    if filepath.exists() == False:
        print(f"{filename} could not be found in the current working directory")
        return
    
    ciphertext = filepath.read_text().lower()

    ## Create a tentative dictionary mapping of chipertext to plaintext letters (ciphertext1 - CallOfTheWild)
    char_mappings = {
        'b': 't',
        'c': 'f',
        'd': 'x',
        'e': 'g',
        'f': 'w',
        'g': 'd',
        'h': 'p',
        'i': 's',
        'j': 'b',
        'k': 'r',
        'l': 'a',
        'm': 'y',
        'n': 'l',
        'o': 'u',
        'p': 'n',
        'q': 'v',
        'r': 'o',
        's': 'm',
        't': 'z',
        'u': 'i',
        'v': 'z',
        'w': 'h',
        'x': 'e',
        'y': 'c',
        'z': 'k',
    }

    ## Define the punctuation to preserve in the ciphertext
    punctuation_to_preserve = {" ", "\n", "'", ",", "."}

    ## Replace each char in the ciphertext with its mapping
    textstring = ""
    for char in ciphertext: 
        if char in char_mappings.keys():                  
            textstring = textstring + char_mappings[char]
        elif char in punctuation_to_preserve:
            textstring = textstring + char
        else:
            textstring = textstring + " "

    ## Write the output to a test file
    with open("test.txt", "w") as file:
        file.write(textstring)
       
main()