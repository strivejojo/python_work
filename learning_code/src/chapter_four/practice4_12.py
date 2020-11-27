my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print(f"My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print(f"\nMy friend's favorite foods are:")
for friends_food in friends_foods:
    print(friends_food)
