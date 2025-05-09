x = int(input("Zadej číslo: "))
y = int(input("Zadej číslo: "))
for i in range(x + 1, y):
    print(i)
else:
    print(f"Žádné číslo není mezi {x} a {y}")