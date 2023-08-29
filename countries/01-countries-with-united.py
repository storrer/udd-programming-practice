# What are all of the countries that have “United” in the name?

with open('countries.txt', 'r') as file:
    countries = file.readlines()

united_countries = []
substring = "United"
for country in countries:
    if country.count(substring):
        united_countries.append(country.rstrip())

print(united_countries)