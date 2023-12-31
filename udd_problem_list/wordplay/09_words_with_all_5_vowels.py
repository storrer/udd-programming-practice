# What are all of the words that have all 5 vowels, in any order?
input_filename = "sowpods.txt"

def find_words_with_each_vowel(filename):
    words_with_each_vowel = []
    vowels = "AEIOU"

    with open(filename, 'r') as file:
        words = file.readlines()
    for word in words:
        # Check if all vowels are present
        contains_each_vowel = True
        
        for vowel in vowels:
            if word.count(vowel) == 0:
                contains_each_vowel = False
                break
        
        if contains_each_vowel:
            words_with_each_vowel.append(word.strip())
    
    return words_with_each_vowel

for word in find_words_with_each_vowel(input_filename):
    print(word)