# 三种出路
prompt = "\nPlease enter your age: "
prompt += "\n(Enter 'quit' when you finished.)"

age = 0
money = 0
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("It's free for the children.")
        elif 3 <= age <= 12:
            money = 10
        elif age > 12:
            money = 15

        if age >= 3:
            print(f"It's {money} dollars.")

