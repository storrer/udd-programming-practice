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


# There may be a tie for longest so we will code accordingly
def find_longest_words(words_list):
    # Assume the first word is the longest   
    longest_length = len(words_list[0])
    longest_words = [words_list[0]]
    
    # Begin looping with 
    for word in words_list[1:]:
        word_length = len(word)
        # If we find a shorter word, re-assign out result array to that word
        if word_length > longest_length:
            longest_length = word_length
            longest_words = [word] 
        elif word_length == longest_length:
            longest_words.append(word)
    
    return longest_words


vowel_free_words = find_words_without_vowels(input_filename)
longest_words = find_longest_words(vowel_free_words)

print("The longest word(s) without any vowels: ", longest_words)
print("The length of the longest word(s) without any vowels: ", len(longest_words[0]), " letters")

# If we want to count 'Y' as a vowel:
def find_words_without_vowels_even_Y(filename):
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

vowel_and_Y_free_words = find_words_without_vowels_even_Y(input_filename)
longest_words = find_longest_words(vowel_and_Y_free_words)
print("The longest word(s) without any vowels even 'Y': ", longest_words)
print("The length of the longest word(s) without any vowels even 'Y': ", len(longest_words[0]), " letters")