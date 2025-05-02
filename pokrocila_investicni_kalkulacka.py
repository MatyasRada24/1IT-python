def spocitej_investici(puvodni_castka, zhodnoceni, n, vklad):
    mesicni_urok = zhodnoceni / 100 / 12
    pocet_mesicu = n * 12

    konecna_castka = puvodni_castka * (1 + mesicni_urok) ** pocet_mesicu

    # Přičteme budoucí hodnotu měsíčních vkladů
    for i in range(1, pocet_mesicu + 1):
        konecna_castka += vklad * (1 + mesicni_urok) ** (pocet_mesicu - i)

    return konecna_castka

# Vstup od uživatele
puvodni_castka = float(input("Zadejte původní částku (v Kč): "))
zhodnoceni = float(input("Zadejte roční zhodnocení (v %): "))
n = int(input("Zadejte počet let: "))
vklad = float(input("Zadejte měsíční vklad (v Kč): "))

vysledek = spocitej_investici(puvodni_castka, zhodnoceni, n, vklad)
print(f"Po {n} letech bude částka činit přibližně {vysledek:.2f} Kč.")

*Silná pomoc od Chat GPT*
