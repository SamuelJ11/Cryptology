from pathlib import Path
import string
import sys

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

main()
