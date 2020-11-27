odd_nums = list(range(1,20,2))
for odd_num in odd_nums:
    print(odd_num)

print(f"The first three items in the list are:{odd_nums[0:3]}")
print(f"Three items from the middle of the list are：{odd_nums[(len(odd_nums)-1)//2:(len(odd_nums)-1)//2+3]}")
print(f"The last three items in the list are:{odd_nums[-3:]}")
