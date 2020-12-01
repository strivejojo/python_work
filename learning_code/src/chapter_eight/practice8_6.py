# 城市名
def city_country(name, country):
    """描述一个城市以其国家"""
    message = f"{name.title()} is in {country.title()}"
    return message


city = city_country('santiago', 'chile')
print(city)

city = city_country('reykjavik', 'iceland')
print(city)

city = city_country('punta arenas', 'chile')
print(city)
