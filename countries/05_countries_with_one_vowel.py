# What countries use only one vowel in their name (the vowel can be used multiple times)

with open('countries.txt','r') as file:
    countries = file.readlines()

one_vowel_countries = []

vowels = 'AEIOU'

for country in countries:
    country = country.rstrip().upper()
    # for each vowel, check if it is present in the word
    for vowel in vowels:
        if country.count(vowel):
            # If it is present, create a string of all the other vowels using replace
            current_vowels = vowels.replace(vowel,'')
            # For each letter in the present country, check that none of them are one of the other vowels
            if all(letter not in current_vowels for letter in country):
                one_vowel_countries.append(country)

for country in one_vowel_countries:
    print(country)