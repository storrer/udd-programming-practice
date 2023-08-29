# What is the shortest baby name in the top 40 baby names for 2020?

shortest_name = []
# reading in the entire file into an array (not great for a large file)
with open('baby_names_2020_short.txt', 'r') as file:
    # names = file.readlines()
    for name in file:
        name = name.rstrip()
        # Guard 
        if not shortest_name:
            shortest_name.append(name)
        # if length of current is shorter than current shortest replace the shortest name
        elif len(name) == len(shortest_name[0]):
            shortest_name.append(name)
        elif len(name) < len(shortest_name[0]):
            shortest_name = [name]

print(shortest_name)

# Don't create unnecessary variables