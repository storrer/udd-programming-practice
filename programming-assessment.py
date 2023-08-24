# Programming assessment scratch pad

# Pseudocode
# What are all of the words that start with a Q, end with a Z, and are less than or equal to 6 letters long?
word_list = "sowpods.txt"

with open(word_list, 'r') as file:
    words = file.readlines()

matching_words = []

# loop over the words
for word in words:
    word = word.rstrip()
    # if starts with q and ends with z and < 7 charcters long
    if word.startswith('Q') and word.endswith('Z') and len(word) < 7:
        matching_words.append(word)

print(matching_words)

# create and print words with U and no other vowel

result_array = []

# iterate through words
for word in words:
    word = word.rstrip()
    # if they contain U and do not contain other vowels append them to result array
    if word.count('U') and all(letter not in 'AEIO' for letter in word):
        result_array.append(word)

print(result_array)

# last array

# create and print an array with words that contain only one kind of vowel
# iterate over words
third_array = []
vowels = 'AEIOU'
for word in words:
    word = word.rstrip()
    # for each vowel in vowels, check if it is the only vowel
    for vowel in vowels:
        if word.count(vowel):
            current_vowels = vowels.replace(vowel, '')
            if all(letter not in current_vowels for letter in word):
                third_array.append(word)

print(third_array)
                    
        
        # if word.count('one vowel') and no other vowels, add it to my list

