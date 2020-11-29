# 城市
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },

    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },

    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        },

    }

for city,city_infos in cities.items():
    country = city_infos['country']
    population = city_infos['population']
    mountain = city_infos['nearby mountains']

    print(f"\n{city.title()} is in {country}.")
    print(f"It has a population of about {population}.")
    print(f"The {mountain} mounats are nearby.")
