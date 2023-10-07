# What are all of the words with no vowel and not even a Y?
input_filename = "sowpods.txt"

def find_words_without_vowels(filename):
    words_without_vowels_even_Y = []
    vowels = "AEIOUY"
    with open(filename, 'r') as file:
        words = file.readlines()
    for word in words:
        for vowel in vowels:
            if vowel in word:
                break
        else:
            words_without_vowels_even_Y.append(word.strip())
    
    return words_without_vowels_even_Y

for word in find_words_without_vowels(input_filename):
    print(word)