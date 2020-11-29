# 喜欢的数2
favorite_nums = {
    'mhx': [2, 3, 4, 0],
    'lxx': [234, 9183, 123556],
    'cyy': [1321, 1516, 1637859],
    'yyy': [114],
    'ld': [2341, 156],
    }

for name,nums in favorite_nums.items():
    print('\n')
    if len(nums) == 1:
        print(f"{name.title()}'s favorite number is:")
    else:
        print(f"{name.title()}'s favorite numbers are:")
    for num in nums:
        print(f"- {num}")
