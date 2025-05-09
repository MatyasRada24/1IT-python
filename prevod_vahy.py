vaha = float(input("Zadej svojí váhu: "))
typ_vahy = str(input("Je tvoje váha v kilogramech nebo librách? (zadej kg nebo lb): "))
if typ_vahy == "kg":
    vypocet1 = vaha * 2.20462
    print(f"Tvoje váha v librech je: {vypocet1}")

elif typ_vahy == "lb":
    vypocet2 = vaha / 2.20462
    print(f"Tvoje váha v kilogramech je: {vypocet2}")

else:
    print("Někde se stala chyba. Zkus to znovu. ")