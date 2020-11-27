guests = ['guido van rossum', 'jack turner', 'lynn hill']

guests.insert(0,'jojo')
guests.insert(2,'Miss Li')
guests.append('eve')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

name = guests.pop(0)
print(f"\nSorry,{name}")

name = guests.pop(0)
print(f"Sorry,{name}")

name = guests.pop(-1)
print(f"Sorry,{name}")

name = guests.pop(-1)
print(f"Sorry, {name}\n")

name = guests[0]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"{name}, please come to dinner")

del guests[0]
del guests[0]
print(guests)
