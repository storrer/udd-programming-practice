# What is the shortest word that contains all 5 vowels?
input_filename = "sowpods.txt"

# Using a function I wrote for problem 09:
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
            words_with_each_vowel.append(word.rstrip())
    
    return words_with_each_vowel

# There may be a tie for shortest, so let's return a list
def find_shortest_words(words_list): 
    # Assume the first word is the shortest   
    shortest_length = len(words_list[0])
    shortest_words = [words_list[0]]
    
    # Begin looping with 
    for word in words_list[1:]:
        word_length = len(word)
        # If we find a shorter word, re-assign out result array to that word
        if word_length < shortest_length:
            shortest_length = word_length
            shortest_words = [word] 
        elif word_length == shortest_length:
            shortest_words.append(word)
    
    return shortest_words


words_to_compare = find_words_with_each_vowel(input_filename)
shortest_words = find_shortest_words(words_to_compare)

print("The shortest word(s) with all five vowels: ", shortest_words)
print("The length of the shortest word(s): ", len(shortest_words[0]), " letters")