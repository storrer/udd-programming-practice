# What is the longest palindrome?
input_filename = "sowpods.txt"

# Using Python's start, stop, stride feature to manipulate strings.
def is_palindrome(phrase):
    reverse = phrase[::-1]
    if reverse == phrase:
        return True
    else:
        return False


def find_longest_palindromes(filename):
    # We cannot assume any palindromes exist
    longest_palindromes = []
    longest_length = 0
    with open(filename, 'r') as file:
        words = file.readlines()
    
    # loop through and compare word lengths
    for word in words:
        if is_palindrome(word.strip()):
            print(f"Palindrome found: {word.strip()}")
            word_length = len(word.strip())
            if word_length > longest_length:
                longest_length = word_length
                longest_palindromes = [word.strip()]
            elif word_length == longest_length:
                longest_palindromes.append(word.strip())

    return longest_palindromes

longest_palindromes = find_longest_palindromes(input_filename)

if len(longest_palindromes) == 0:
    print("No palindromes found in file.")
else:
    print("The longest palindrome(s)")
    for palindrome in longest_palindromes:
        print(palindrome)

