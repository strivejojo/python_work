# 人生的不同阶段
age = 100
if age < 2:
    this_one = 'baby'
elif 2 <= age < 4:
    this_one = 'kid'
elif 4 <= age < 13:
    this_one = 'child'
elif 13 <= age < 20:
    this_one = 'teenager'
elif 20 <= age < 65:
    this_one = 'adult'
else:
    this_one = 'old man'

print(f"this man is a {this_one}")
