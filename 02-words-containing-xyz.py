# What are all of the words containing an X and a Y and a Z?
input_filename = "sowpods.txt"

def find_words_with_XYZ(filename):
    words_with_XYZ = []
    with open(filename, 'r') as file:
        words = file.readlines()
    
    for word in words:
        if word.count("X") and word.count("Y") and word.count("Z"):
            words_with_XYZ.append(word.strip())
    
    return words_with_XYZ

for word in find_words_with_XYZ(input_filename):
    print(word)