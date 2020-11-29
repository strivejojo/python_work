#河流
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada'
    }

for country,river in rivers.items():
    print(f"The {country.title()} runs through {river.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
