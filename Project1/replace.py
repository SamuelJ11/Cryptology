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

    ## Create a tentative dictionary mapping of chipertext to plaintext letters (ciphertext1 - Hamlet)
    char_mappings = {
        ',': ',', #dont change commas
        '.': '.', #dont change periods
        'b': 't', 
        'w': 'h',  
        'x': 'e', 
        'l': 'o',
    }

    ## Replace each char in the ciphertext with its mapping
    textstring = ""
    for char in ciphertext: 
        if char in char_mappings.keys():                  
            textstring = textstring + char_mappings[char]
        else:
            textstring = textstring + "_"

    ## Write the output to a test file
    with open("test.txt", "w") as file:
        file.write(textstring)
       
main()