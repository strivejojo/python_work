# 披萨配料
prompt = "\nPlease enter the name of a pizza:"
prompt += "\n(enter 'quit' when you are finished.)"

pizza = ''

while pizza != 'quit':
    pizza = input(prompt)
    if pizza != 'quit':
        print(pizza)
