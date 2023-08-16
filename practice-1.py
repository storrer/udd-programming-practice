# list all words that start with q end with z less than or equal to 6 letters long
input_filename = 'sowpods.txt'

# define a function
def list_words_q_start_z_end_max_length_six(filename):
    # create result
    matching_words = []

    # read file
    with open(filename, 'r') as file:
        words = file.readlines()

    # loop over words
    for word in words:
        word = word.rstrip()
        # if word starts with Q AND word ends with Z AND word length is less than or equal to 6
        if word.startswith('Q') and word.endswith('Z') and len(word) < 7:
            matching_words.append(word)

    return matching_words

print(list_words_q_start_z_end_max_length_six(input_filename))