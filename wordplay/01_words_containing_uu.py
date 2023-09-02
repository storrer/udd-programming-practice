# What are all of the words containing UU?
input_filename = "sowpods.txt"

def find_words_with_UU(filename):
    words_with_UU = []
    with open(filename, 'r') as file:
        words = file.readlines()
    
    for word in words:
        if word.count("UU"):
            words_with_UU.append(word.strip())
    
    return words_with_UU

for word in find_words_with_UU(input_filename):
    print(word)
