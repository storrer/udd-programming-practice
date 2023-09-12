"""
What is the longest word that can be made without the letters in “AEIOSHRTN” 
(in other words, without the most common letters)? Make sure your solution 
can handle ties.
"""

def contains_no_banned_letters(word: str):
    banned_letters = "AEIOSHRTN"
    return all(letter not in banned_letters for letter in word)



def find_longest_words(array):
    longest_words = []
    
    # Read through input word by word
    for word in array:
        # Strip white space from words
        word = word.rstrip()
        # If word is shorter than max_length (longest words)
        if longest_words and len(word) < len(longest_words[0]): # guard clause
            continue    
        if contains_no_banned_letters(word):
            if not longest_words or len(word) > len(longest_words[0]): 
                longest_words = [word]
            else:
                # If it is the same length, i.e. a tie
                longest_words.append(word)
    return longest_words
# “AEIOSHRTN”
test1 = ['DUG', 'BUCK', 'CUFF'] # buck, cuff , length = 4

longest_words = find_longest_words(test1)
print(f"Test1: max length: {len(longest_words[0])} and longest words: {longest_words}")

    # longest words result variable = []
        # If word matches our criteria:
        # function: For each letter, ensure that the letter in banned letters
        # If it is longer than max_length, reassign the longest word variable, and reassign the max_length variable
        # elif it is the same length as max_length, append this word to result variable (handle ties)
with open('sowpods.txt', 'r') as file:
    longest_words = find_longest_words(file)
    

print(f"sowpods.txt: max length: {len(longest_words[0])} and longest words: {longest_words}")

#TODO #1 write unit