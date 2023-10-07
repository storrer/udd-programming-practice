# What are all of the words that start with “PRO”, end in “ING”, and are exactly 11 letters long?            

# Function validating words
def word_matches(word: str):
    return len(word) == 11 and word.startswith("PRO") and word.endswith("ING")

# Read in the file line by line/ word by word
with open('sowpods.txt', 'r') as file:
    for word in file:
        # strip white space from the right side
        word = word.rstrip()
        if word_matches(word):
            print(word) 

#TODO reevaluate comments