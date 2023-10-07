# What are all of the names that were top 40 baby names in both 1880 and 2020?

# Read in 1880
with open('E:\\Projects\\udd-programming-practice\\baby-names\\baby_names_1880_short.txt', 'r') as file:
    # create a set from names   
    names_1880 = set(file.readlines())

if names_1880:
    print("Pass")
else:
    print(names_1880)

# read in 2020
with open('E:\\Projects\\udd-programming-practice\\baby-names\\baby_names_2020_short.txt', 'r') as file_two:
    # create a set from names
    names_2020 = set(file_two.readlines())

empty_list = []
assert not empty_list
# Assumption of length 40
assert len(names_2020) == 40

#TODO come up with a better variable
names_in_both_eras = []

# compare sets for names appearing in both
# 1. for loop to append names appearing in both to a result list
for name in names_1880:
    if name in names_2020:
        names_in_both_eras.append(name)

# 2. Use a union to retrieve the members present in both sets

# Print names appearing in both sets
print(*names_in_both_eras)
