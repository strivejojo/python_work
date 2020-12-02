# 三明治
def make_sandwich(*toppings):
    """制作一个三明治"""
    print(f"\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
