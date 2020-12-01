# 梦想的度假胜地
responses = {}
active = True

while active:
    name = input('\nWhat is your name: ')
    vacation_location = input('\nIf you could visit one place in the world,'
                              'where would you go?')

    responses[name] = vacation_location

    repeat = input('Would you like to let anthor person respond?(Yes/No):')
    if repeat.lower() == 'no':
        active = False

print("\n--- Poll Results ---")
for name,vacation_location in responses.items():
    print(f"-name:{name} place:{vacation_location}")
