# 餐馆订位
customer_num = input('How many people do you come to have a table: ')
customer_num = int(customer_num)
if customer_num > 8:
    print(f"We don't have a empty table.")
elif customer_num <= 8:
    print(f"Welcome to our resturant.")
