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
    filename = str(sys.argv[1] + ".txt")
    cwd = Path().resolve() 
    filepath = cwd.joinpath(filename)   

    ## Check if the path for the provided filename exists in the current directory
    if filepath.exists() == False:
        print(f"{filename} could not be found in the current working directory")
        return

        ## PROCESS ONEGRAMS ###

    ## Define the alphabet and punctuation to preserve
    alphabet = set(string.ascii_lowercase)
    punctuation_to_preserve = {" ", "\n", "\n\n", "'", ","}
 
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

    ## Create a common text for bigrams and trigrams by removing every non-alphabetic character that is not whitelisted from the text
    multigram_text = filepath.read_text().lower()    
    for char in multigram_text:
        if (char not in punctuation_to_preserve and char not in alphabet):
            multigram_text = multigram_text.replace(char, "")

        ## PROCESS BIGRAMS ###

    ## Prepare a list of bigrams of the form ['bigram', 'bigram' . . .]
    bigram_list = []
    for i in range(len(multigram_text) - 1):
        first = multigram_text[i]
        second = multigram_text[i+1]

        if (first in alphabet and second in alphabet):
            bigram_string = first + second
            bigram_list.append(bigram_string)

    ## Use the Counter class to get a count of every bigram in the text
    bigram_counts = Counter(bigram_list)

    ## Convert the Counter object to a dictionary and sort the dictionary by value in descending order
    bigram_dict = {}
    for bigram in bigram_counts:
        bigram_dict[bigram] = bigram_counts[bigram]
    bigram_dict = dict(sorted(bigram_dict.items(), key = operator.itemgetter(1), reverse = True))

        ### PROCESS TRIGRAMS ###

    ## Prepare a list of trigrams of the form ['trigram', 'trigram' . . .]
    trigram_list = []
    for i in range(len(multigram_text) - 2):
        first = multigram_text[i]
        second = multigram_text[i+1]
        third = multigram_text[i+2]

        if (first in alphabet and second in alphabet and third in alphabet):
            trigram_string = first + second + third
            trigram_list.append(trigram_string)

    ## Use the Counter class to get a count of every trigram in the text
    trigram_counts = Counter(trigram_list)

    ## Convert the Counter object to a dictionary and sort the dictionary by value in descending order
    trigram_dict = {}
    for trigram in trigram_counts:
        trigram_dict[trigram] = trigram_counts[trigram]
    trigram_dict = dict(sorted(trigram_dict.items(), key = operator.itemgetter(1), reverse = True))

        ## TABULATE THE DATA ###

    ## Initialze the table
    Table = PrettyTable()

    ## Create the first column
    index_column = []
    for i in range(1, 27):
        index_column.append(i)

    Table.add_column("Index", index_column)

    ## Create the second and third column
    onegram_columnkeys = []
    onegram_columnvalues = []
    for key, value in charcount_dict.items():
        onegram_columnkeys.append(key)
        onegram_columnvalues.append(value)

    Table.add_column("Onegram", onegram_columnkeys)
    Table.add_column("Counts", onegram_columnvalues)

    ## Create the fourth and fifth column
    bigram_columnkeys = []
    bigram_columnvalues = []
    for key, value in bigram_dict.items():
        bigram_columnkeys.append(key)
        bigram_columnvalues.append(value)
    
    Table.add_column("Bigram", bigram_columnkeys[0:26])
    Table.add_column("Counts", bigram_columnvalues[0:26])

    ## Create the last two columns
    trigram_columnkeys = []
    trigram_columnvalues = []
    for key, value in trigram_dict.items():
        trigram_columnkeys.append(key)
        trigram_columnvalues.append(value)
    
    Table.add_column("Trigram", trigram_columnkeys[0:26])
    Table.add_column("Counts", trigram_columnvalues[0:26])
    
    print(Table)

main()