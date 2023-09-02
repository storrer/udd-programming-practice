# What countries both begin and end with a vowel?

with open('countries.txt', 'r') as file:
    countries = file.readlines()

bookended_by_vowels = []
vowels = tuple('AEIOUaeiou')

# loop over the countries
for country in countries:
    country = country.rstrip()
    # if both starts with and endswith vowels
    if country.startswith(vowels) and country.endswith(vowels):
        bookended_by_vowels.append(country)

for country in bookended_by_vowels:
    print(country)