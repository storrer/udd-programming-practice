# What are all of the words that both start and end with a Y?

input_filename = "sowpods.txt"

def find_words_starting_and_ending_with_Y(filename):
    words_starting_and_ending_with_Y = []
    with open(filename, 'r') as file:
        words = file.readlines()
    
    for word in words:
        # Access start and end of the words with [0] and [-2]
        if word[0] == 'Y' and word[-2] == 'Y':
            words_starting_and_ending_with_Y.append(word.strip()) 
    
    return words_starting_and_ending_with_Y

for word in find_words_starting_and_ending_with_Y(input_filename):
    print(word)