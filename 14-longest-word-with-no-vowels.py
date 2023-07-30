# What is the longest word that contains no vowels?
input_filename = "sowpods.txt"

# From problem 08
def find_words_without_vowels(filename):
    words_without_vowels = []
    vowels = "AEIOU"
    with open(filename, 'r') as file:
        words = file.readlines()
    for word in words:
        for vowel in vowels:
            if vowel in word:
                break
        else:
            words_without_vowels.append(word.strip())
    
    return words_without_vowels

vowel_free_words = find_words_without_vowels(input_filename)
