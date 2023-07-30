# Create and print an array containing all of the words that end in "GHTLY"
input_filename = "sowpods.txt"
query_string = "GHTLY"

def find_words_ending_with_substring(filename, substring):
    words_ending_with_substring = []

    with open(filename, 'r') as file:
        words = file.readlines()

    for word in words:
        # Python comes with endswith(), conveniently
        if word.strip().endswith(substring):
            words_ending_with_substring.append(word.strip())

    return words_ending_with_substring

result = find_words_ending_with_substring(input_filename, query_string)
print("Here is an array of all words ending in 'GHTLY': ", result)

