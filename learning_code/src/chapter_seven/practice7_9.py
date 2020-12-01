# 五香烟熏牛肉卖完了
print(f"Pastrami is sold out.\n")

sandwich_orders = ['veggie', 'pastrami', 'grilled cheese', 'turkey',
                   'roast beef', 'pastrami', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made you {finished_sandwich} sandwich.")
    finished_sandwiches.append(finished_sandwich)

for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} is done.")
