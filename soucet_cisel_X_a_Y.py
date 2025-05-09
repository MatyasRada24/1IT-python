x = int(input("Zadej libovolné číslo. "))
y = int(input("Zadej libovolné číslo. "))
soucet = 0
for i in range(x, y):
    soucet += i
print(f"Součet čílel mexi {x} a {y} je: {soucet}.")