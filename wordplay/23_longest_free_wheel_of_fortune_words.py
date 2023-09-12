"""
What is the longest word that can be made from only the letters in “RSTLNE”? 
Not all of those letters need to be used, and letters can be repeated. Make 
sure your solution can handle ties.
"""
# O(l), l = number of letters in word
def word_matches_all(word: str):
    free_letters = 'RSTLNE'
    return all(letter in free_letters for letter in word)

# O(w), w = number of words in array
def find_longest_match(array):
    max_length = 0
    longest_words = []

    for word in array:
        if word_matches_all(word):
            if len(word) == max_length:
                longest_words.append(word)
            elif len(word) > max_length:
                max_length = len(word)
                longest_words = [word]
    return (max_length,longest_words)
# l * w 
test1 = ['REST', 'NEST', 'NET', 'SET']

max_length, longest_words = find_longest_match(test1)

print(f"Max length: {max_length}", f"Longest words: {longest_words}")

max_length = 0
longest_words = []
with open('sowpods.txt', 'r') as file:
    # words = file.readlines()
    for word in file:
        # strip white space from the right side
        word = word.rstrip()
        if word_matches_all(word):
            if len(word) == max_length:
                longest_words.append(word)
            elif len(word) > max_length:
                max_length = len(word)
                longest_words = [word]

print(f"Max length: {max_length}", f"Longest words: {longest_words}")

