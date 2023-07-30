# What are all of the words containing a Q but not a U?
input_filename = "sowpods.txt"

def find_words_with_Q_not_U(filename):
    words_with_Q_not_U = []
    with open(filename, 'r') as file:
        words = file.readlines()
    
    for word in words:
        if word.count("Q") and not word.count("U"):
            words_with_Q_not_U.append(word.strip())
    
    return words_with_Q_not_U

for word in find_words_with_Q_not_U(input_filename):
    print(word)