# What are the longest baby names in the top 40 baby names for 2020? Make sure 
# you can handle if there’s a tie.
longest_names = []
# reading in the entire file into an array (not great for a large file)
with open('baby_names_2020_short.txt', 'r') as file:
    # names = file.readlines()
    for name in file:
        name = name.rstrip()
        # Guard 
        if not longest_names:
            longest_names.append(name)
        # if length of current is longer, reassign the result list
        elif len(name) == len(longest_names[0]):
            longest_names.append(name)
        elif len(name) > len(longest_names[0]):
            longest_names = [name]

print(longest_names)