import string
import sys
from pathlib import Path
from collections import Counter
from prettytable import PrettyTable
import operator

def main():

    # Check for valid program usage
    if len(sys.argv) != 2:
        print("Usage: myscript.py <filename>")
        return
    
    ## Define the alphabet and punctuation to preserve
    alphabet = set(string.ascii_lowercase)
    punctuation_to_preserve = {" ", "\n", "\n\n", "'", ","}

    ## Import and read filename for analysis
    filename = str(sys.argv[1] + ".txt")
    cwd = Path().resolve() 
    filepath = cwd.joinpath(filename)   

    ## Check if the path for the provided filename exists in the current directory
    if filepath.exists() == False:
        print(f"{filename} could not be found in the current working directory")
        return

        ## PROCESS ONEGRAMS
 
    ## Remove every non-alphabetic character from the text
    onegram_text = filepath.read_text().lower()
    for ch in onegram_text:
        if ch not in alphabet:
            onegram_text = onegram_text.replace(ch, "")

    ## Use the Counter class to get a count of every character in the text
    char_counts = Counter(onegram_text)

    ## Convert the Counter object to a dictionary and sort the dictionary by value in descending order
    charcount_dict = {}
    for onegram in char_counts:
        charcount_dict[onegram] = char_counts[onegram]
    charcount_dict = dict(sorted(charcount_dict.items(), key = operator.itemgetter(1), reverse = True))

    ## Prepare a 2D list of the form [[1, 'letter', 'count'], [2, 'letter', 'count'] . . .]
    charcount_list = []    
    for index, (key, value) in enumerate(charcount_dict.items(), start = 1):
        charcount_list.append([index, key, value])       

    ## Make a "prettytable" from the charcount_list
    table = PrettyTable(["Index", "Onegrams", "Counts"]) 
    for list in charcount_list:
        table.add_row([list[0], list[1], list[2]])
    
    print(table)

        ## PROCESS BIGRAMS AND TRIGRAMS

    multigram_text = filepath.read_text().lower()
    
    for char in multigram_text:
        if (char not in punctuation_to_preserve and char not in alphabet):
            multigram_text = multigram_text.replace(char, "")
    
    print(multigram_text[0:200])

main()