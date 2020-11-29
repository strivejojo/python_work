#调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

search_persons = ['jen', 'sarah', 'mhx', 'lxx']

for name, languege in favorite_languages.items():
    print(f"{name.title()}'s favorite languege is {languege.title()}.")

print('')

for search_person in search_persons:
    if search_person in favorite_languages.keys():
        print(f"{search_person.title()},Thank You")
    else:
        print(f"{search_person.title()},Please")
