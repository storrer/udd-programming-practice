# [ ] There is at least one country name that contains another country name. Find all of these cases.

with open('countries.txt','r') as file:
    countries = file.readlines()

countries_containing_countries = []

"""
for country in countries:
    for other_country in countries:
        # if country equals other_country, skip
        if country == other_country:
            continue
        elif country.count(other_country): # count() works like a flag
            countries_containing_countries.append(country)
"""
# let's do rstrip, though
for country in countries:
    country = country.rstrip()
    for other_country in countries:
        other_country = other_country.rstrip()
        # if country equals other_country, skip
        if country == other_country:
            continue
        elif country.count(other_country): 
            countries_containing_countries.append(country)
for item in countries_containing_countries:
    print(item)