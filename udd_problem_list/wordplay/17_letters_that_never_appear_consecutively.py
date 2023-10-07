"""
What are all of the letters that never appear consecutively in an English word?
For example, we know that “U” is not an answer, because of the word VACUUM, and we know that “A” is not an answer, because of “AARDVARK”, but which letters never appear consecutively?

"""
input_filename = "sowpods.txt"

#
def find_letters_never_consecutive(filename):
    # We'll use sets to make finding the difference easier later
    consecutive_letters = set()
    # Sets do not allow duplicates
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    with open(filename, 'r') as file:
        words = file.readlines()
    
    for word in words:
        word = word.strip()
        preceding_letter = None
        for letter in word:
            if letter == preceding_letter:
                consecutive_letters.add(letter)
            preceding_letter = letter

    # Find the letters that do not appear consecutively
    never_consecutive_letters = alphabet - consecutive_letters
    return never_consecutive_letters

non_consecutive_letters = find_letters_never_consecutive(input_filename)
print("Letters that never appear consecutively in the input file: ", non_consecutive_letters)