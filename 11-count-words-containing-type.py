# How many words contain the substring "TYPE”?
input_filename = "sowpods.txt"
query_string = "TYPE"

# Let's write a generic function, just in case
def count_words_with_substring(filename, substring):
    count = 0
    with open(filename, 'r') as file:
        words = file.readlines()

    for word in words:
        if substring in word:
            count += 1

    return count

result = count_words_with_substring(input_filename, query_string)
print("Number of words with substring 'TYPE': ", result)