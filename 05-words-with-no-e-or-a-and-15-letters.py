# What are all of the words that have no E or A and are at least 15 letters long?

input_filename = "sowpods.txt"

def find_long_words_without_E_or_A(filename):
    long_words_without_E_or_A = []
    with open(filename, 'r') as file:
        words = file.readlines()
    
    for word in words:
        # I read that word.count() is faster but it sure takes a lot of typing
        if (word.count("E") == 0) and (word.count("A") == 0) and len(word.strip()) > 14:
            long_words_without_E_or_A.append(word.strip()) 
    
    return long_words_without_E_or_A

for word in find_long_words_without_E_or_A(input_filename):
    print(word)