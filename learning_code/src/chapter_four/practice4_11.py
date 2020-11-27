my_foods = ['banana','chicken','water']
friend_foods = my_foods[:]

my_foods.append('noodles')
friend_foods.append('pizza')

print(f"My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print(f"\nFriend‘s favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)
