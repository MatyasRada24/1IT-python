puvodni_castka = float(input("Zadejte původní částku (v Kč): "))
zhodnoceni = float(input("Zadejte roční zhodnocení (v %): "))
n = int(input("Zadejte počet let: "))

castka = puvodni_castka

for n in range(1, n + 1):
    urok = castka * (zhodnoceni / 100)
    castka = castka + urok

    print(f"Po {n}. roce: {castka:.2f} Kč")