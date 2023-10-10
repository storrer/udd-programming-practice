# Words containing only E and at least 15 letters long

# Read in the file line by line


def contains_only_es_length_fifteen(word):
    wrong_vowels = 'AUIO'
    if len(word) < 15:
        return False
    for letter in word:
        if letter in wrong_vowels:
            return False
    return 'E' in word
        

with open('sowpods.txt', 'r') as file:
    # For each letter in a word, 
    for word in file:
        word = word.rstrip()
        if contains_only_es_length_fifteen(word):
            print(word)