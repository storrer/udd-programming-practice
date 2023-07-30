# What are all of the words that have all 5 vowels, in alphabetical order?

# A function that determines if a word meets our criteria
def has_vowels_in_order(word):
    vowels = 'AEIOU'
    previous_vowel_index = -1

    for vowel in vowels:
        vowel_index = word.find(vowel)
        if vowel_index == -1 or vowel_index < previous_vowel_index:
            return False
        previous_vowel_index = vowel_index

    return True

# Starting with the function I wrote for problem 09
def find_words_with_each_vowels(filename):
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


def find_words_with_each_vowel_in_order(word_list):
    words_with_each_vowel_in_order = []

    for word in word_list:
        if has_vowels_in_order(word):
            words_with_each_vowel_in_order.append(word)

    return words_with_each_vowel_in_order

input_filename = "sowpods.txt"
words_list = find_words_with_each_vowels(input_filename)
result = find_words_with_each_vowel_in_order(words_list)
print("Words with each vowel in alphabetical order are:")

for word in result:
    print(word)
