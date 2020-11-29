# 人们
myself = {
    'first_name': 'M',
    'last_name': 'HX',
    'age': '22',
    'city': 'GuangZhou',
    }

one_girl = {
    'first_name': 'L',
    'last_name': 'XX',
    'age': '23',
    'city': 'ChongQing',
    }

yesterday_girl = {
    'first_name': 'C',
    'last_name': 'YY',
    'age': '23',
    'city': 'ZhengZhou',
}

people_lists = [myself, one_girl, yesterday_girl]
for people in people_lists:
    full_name = f"{people['first_name']}{people['last_name']}"
    print(f"{full_name} {people['age']} {people['city']}")
