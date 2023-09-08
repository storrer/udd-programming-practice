"""
What are all of the words that can be made from only the letters in “RSTLNE”?
Not all of those letters need to be used, and letters can be repeated.
"""

# Function validating words
def word_matches(word: str):
    # iterate through the word letter by letter
    for letter in word:
    #TODO use all()
        # if the letter is not in 'RSTLNE' return False
        if letter not in 'RSTLNE':
            return False
    
    # otherwise return True
    return True
    #TODO tidy this up into one line expression

def word_matches_all(word: str):
    free_letters = 'RSTLNE'
    return all(letter in free_letters for letter in word)

def word_match_unique(word: str):
    free_letters = 'RSTLNE'
    
    seen_rstlne = set()
    # Iterate over word letter by letter
    for letter in word:
        if letter not in free_letters:
            return False
        if letter in seen_rstlne:
            return False
        seen_rstlne.add(letter)

    return True

# Read in the file line by line/ word by word
with open('sowpods.txt', 'r') as file:
    for word in file:
        # strip white space from the right side
        word = word.rstrip()
        if word_match_unique(word):
            print(word)

input_test = ['REST', 'REEL', 'ZZZ']

for word in input_test:
    print(word_match_unique(word))
