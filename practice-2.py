# create and print an array that contains the words with U and no other vowel

# create result

# read in file

# iterate over words

# rstrip words 

# if 'U' is in the word and all(letter not in 'AEIO' for letter in word)
# create result
matching_words = []

# read file
with open('sowpods.txt', 'r') as file:
    words = file.readlines()

# loop over words
for word in words:
    word = word.rstrip()
    # if u is in the word and no other vowels are in the word
    if word.count('U') == 1 and all(letter not in 'AEIO' for letter in word):
        matching_words.append(word)

print(matching_words)