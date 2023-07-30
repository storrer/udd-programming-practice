# What are all of the words that have a B and an X and are less than 5 letters long?

input_filename = "sowpods.txt"

def find_short_words_with_B_and_X(filename):
    short_words_with_B_and_X = []
    with open(filename, 'r') as file:
        words = file.readlines()
    
    for word in words:
        # Using if-in to check for letters
        if (len(word.strip()) < 5) and "B" in word and "X" in word:
            short_words_with_B_and_X.append(word.strip()) 
    
    return short_words_with_B_and_X

for word in find_short_words_with_B_and_X(input_filename):
    print(word)