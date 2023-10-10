# What are all of the words that have only “U”s for vowels?

# Create result variable
words_with_u_as_only_vowel = []
# Create a list of vowels we do not want

        


def contains_only_us(word):
    wrong_vowels = 'AEIO'
    for letter in word:
        if letter in wrong_vowels:
            return False
    if word.count("U") >= 1: # if "U" in word
        return True
    else:
        return False
    # return "U" in word

# Read in the file line by line

with open('sowpods.txt', 'r') as file:
    # For each letter in a word, 
    for word in file:
        if contains_only_us(word):
            words_with_u_as_only_vowel.append(word)
   # we can print this here
# print the result
print(*words_with_u_as_only_vowel)