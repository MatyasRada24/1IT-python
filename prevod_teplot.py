teplota = float(input("Napiš, jaké je u tebe aktuální teplota: "))
znak = str(input("Napiš, jestli se jedná o stupně Celsia, Fahrenheita, Kelvin (C/F/K): "))
K = 273,15
if znak == "C":
    vypocet1 = (teplota * 9/5) + 32
    print(f"Teplota ve Fahrenheitech je: {vypocet1}.")
elif znak == "F":
    vypocet2 = (teplota - 32) * 5/9
    print(f"Teplota ve Celsiích je: {vypocet2}.")