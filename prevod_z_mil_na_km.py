vzdalenost = float(input("Zadej vzdálenost: "))
jednotka = str(input("Zadej jednotku (km / mil): "))
if jednotka == "km":
    vysledek = vzdalenost * 0.6213727
    print(f"Převod z km na míle je: {vysledek} ")

if jednotka == "mil":
    vysledek2 = vzdalenost / 1.60934
    print(f"Převod z mil na km je: {vysledek2} ")