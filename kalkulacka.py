x = int(input("Zadejte první číslo: "))
y = int(input("Zadejte druhé číslo: "))
operace = input("Jakou operaci chceš provést? ")
if operace == "+":
    print(x + y)
elif operace == "-":
    print(x - y)
elif operace == "*":
    print(x * y)
elif operace == "/":
    print(x / y)
elif operace == "**":
    print(x ** y)
elif operace == "//":
    print(x // y)
else:
    print("Error. Napiš realnou operaci. (+, -, *, /, **, //)")
