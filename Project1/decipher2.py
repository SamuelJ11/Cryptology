import string, sys, operator
from pathlib import Path
from collections import Counter

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

        ### DEFINE THE CHARACTER MAPPING AND WHITELISTED PUNCTUATION ###

    ## Create a tentative dictionary mapping of chipertext to plaintext letters (ciphertext2 - Hamlet)
    char_mappings = {
        'a': 'c',
        'b': 'i',
        'c': 'o',
        'd': 'v',
        'e': 'y',
        'f': 'b',
        'g': 'l',
        'h': 'k',
        'i': 'f',
        'j': 't',
        'k': 'q',
        'l': 'm',
        'm': 'a',
        'n': 'd',
        'o': 'z',
        'p': 'h',
        'q': 'p',
        'r': 's',
        's': 'j',
        't': 'n',
        'u': 'u',
        'v': 'r',
        'w': 'g',
        'x': 'e',
        'y': 'w',
        'z': 'x'
    }

    ## Define the punctuation to preserve in the ciphertext
    punctuation_to_preserve = {" ", "\n", "'", ",", "."}

        ### DECRYPT THE CIPHERTEXT WITH THE MAPPING AND PRINT OUTPUT TO TERMINAL ###

    ## Replace each char in the ciphertext with its mapping
    textstring = ""
    for char in ciphertext: 
        if char in char_mappings.keys():                  
            textstring = textstring + char_mappings[char]
        elif char in punctuation_to_preserve:
            textstring = textstring + char
        else:
            textstring = textstring + " "

    ## Print the deciphered text and its corresponding codebook to the terminal 
    print("DECRYTPED CIPHERTEXT:\n")
    print(f"{textstring}\n")
    print(f"CHARACTER MAPPINGS FOR {filename}: \n")
    print(char_mappings)

main()