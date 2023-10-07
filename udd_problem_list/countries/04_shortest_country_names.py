# What are the shortest country names, allow for ties?
with open('countries.txt','r') as file:
    countries = file.readlines()

shortest_countries = []

# Let's suppose that the first country is the shortest
shortest_length = len(countries[0].rstrip())

for country in countries:
    country = country.rstrip()
    if len(country) == shortest_length:
        shortest_countries.append(country)
    elif len(country) < shortest_length:
        shortest_length = len(country)
        shortest_countries = [country]

for country in shortest_countries:
    print(country)