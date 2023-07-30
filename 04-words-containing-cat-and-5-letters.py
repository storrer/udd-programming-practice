# What are all of the words that contain the word CAT and are exactly 5 letters long?
input_filename = "sowpods.txt"

def find_five_letter_words_with_CAT(filename):
    five_letter_words_with_CAT = []
    with open(filename, 'r') as file:
        words = file.readlines()
    
    for word in words:
        if word.count("CAT") and len(word.strip()) == 5:
            five_letter_words_with_CAT.append(word.strip())
    
    return five_letter_words_with_CAT

for word in find_five_letter_words_with_CAT(input_filename):
    print(word)