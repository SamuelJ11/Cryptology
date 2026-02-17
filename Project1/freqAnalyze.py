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
    
    ## Define the alphabet
    alphabet = set(string.ascii_lowercase)

    ## Import and read filename for analysis
    filename = str(sys.argv[1] + ".txt")
    cwd = Path().resolve() 
    filepath = cwd.joinpath(filename)   

    ## Check if the path for the provided filename exists in the current directory
    if filepath.exists() == False:
        print(f"{filename} could not be found in the current working directory")
        return

    filename = filepath.read_text().lower()
    
    ## Remove every non-alphabetic character from the text
    for ch in filename:
        if ch not in alphabet:
            filename = filename.replace(ch, "")

    ## Use the Counter class to get a count of every character in the text
    char_counts = Counter(filename)

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
    
main()