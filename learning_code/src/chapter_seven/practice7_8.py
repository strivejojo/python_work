# 熟食店
sandwich_orders = ['veggie', 'grilled cheese', 'turkey','roast beef']
finished_sandwiches=[]

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made you {finished_sandwich} sandwich.")
    finished_sandwiches.append(finished_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} is done.")
