# 喜欢的地方
favorite_palaces = {
    'MHX': ['Guang Zhou', 'Bei Jing', 'Chong Qing'],
    'LXX': ['Chong Qing', 'Qing Dao', 'Hai Nan'],
    'CYY': ['Zheng Zhou', 'Guang Zhou', 'Shang Hai'],
    }

for name, places in favorite_palaces.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place}")
