# What countries use only one vowel in their name (the vowel can be used multiple times)

with open('countries.txt','r') as file:
    countries = file.readlines()

one_vowel_countries = []

vowels = 'AEIOU'

for country in countries:
    country = country.rstrip().upper()
    for vowel in vowels:
        if country.count(vowel):
            current_vowels = vowels.replace(vowel,'')
            if all(letter not in current_vowels for letter in country):
                one_vowel_countries.append(country)

for country in one_vowel_countries:
    print(country)