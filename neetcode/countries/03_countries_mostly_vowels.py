# Countries with mostly vowels ( > 50 % vowels)
with open('countries.txt','r') as file:
    countries = file.readlines()

countries_with_mostly_vowels = []

vowels = 'AEIOU'

for country in countries:
    country = country.rstrip().upper()
    letters = len(country)
    vowel_count = 0
    for vowel in vowels:
        vowel_count += country.count(vowel)
    if vowel_count > (letters/2.0):
        countries_with_mostly_vowels.append(country)

for country in countries_with_mostly_vowels:
    print(country)