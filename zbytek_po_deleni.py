x = int(input("Napiš číslo, které chceš dělit: "))
y = int(input("Napiš číslo, kterým budeš dělit: "))
zbytek = x - (x // y) * y
print(zbytek)