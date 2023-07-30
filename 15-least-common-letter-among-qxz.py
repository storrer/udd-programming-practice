# Which of the letters Q, X, and Z is the least common?
input_filename = "sowpods.txt"
letters_to_compare = ['Q','X','Z']

def find_least_common_substrings(filename, list_of_substrings):
    # Using a dictionary object to count these letters in a single file read.
    substring_frequencies = {}
    # Initialize counters for each item in the input array
    for substring in list_of_substrings:
        substring_frequencies[substring] = 0

    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            # Count the occurrences of each key in the dictionary
            for letter in word:
                if letter in substring_frequencies:
                    substring_frequencies[letter] += 1

    print(f"The occurences for each substring from among {list_of_substrings}")
    print(substring_frequencies)
    # Check for a tie for lowest
    # min() finds the lowest value within an iterable
    lowest_frequency = min(substring_frequencies.values())

    least_common_substrings = {}
    # Loop over the dictionary using .items() to get the key value pairs
    for substring, count in substring_frequencies.items():
        if count == lowest_frequency:
            least_common_substrings[substring] = count

    return least_common_substrings

least_common_letters = find_least_common_substrings(input_filename, letters_to_compare)
print(f"The least common letter(s) from among {letters_to_compare}")
print(least_common_letters)