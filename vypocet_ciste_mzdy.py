print("------------------------------------------------------------------------------------------------")
print("23% daň se vstahuje pouze pro osoby s příjmem nad 131 901Kč za 1 měsíc.")
print("Za děti stát dává daňové zvýhodnění.")
print("Za 1 dítě je sleva 1267Kč")
print("Za 2 děti je sleva 1860Kč")
print("Za 3 děti je sleva 2320Kč")
print("Stát dává pouze slevu na max 3 děti. Pokud máš více než 3 děti, sleva na dani se nezvyšuje.")
print("------------------------------------------------------------------------------------------------")

vyplata = int(input("Zadej svojí hrubou mzdu: "))
dan = int(input("Vyber daň: (15 / 23) "))
deti = int(input("Kolik máš dětí? (0-3) "))

socko =  vyplata * 0.065 # - SOCKO
zdravko = vyplata * 0.045 # - ZDRAVKO
superhruba = vyplata * 1.338
sleva_poplatnik = 2570

if dan == 15 and deti == 0:
    vypocet = vyplata - (socko + zdravko) - (superhruba * 0.15 - sleva_poplatnik)
    print(f"Čistá mzda je: {vypocet} Kč")
else:("Něco se pokazilo, zkus to znovu.")

if dan == 15 and deti == 1:
    vypocet1 = vyplata - (socko + zdravko) - (superhruba * 0.15 - sleva_poplatnik - 1267)
    print(f"Čistá mzda je: {vypocet1} Kč")
else:("Něco se pokazilo, zkus to znovu.")

if dan == 15 and deti == 2:
    vypocet2 = vyplata - (socko + zdravko) - (superhruba * 0.15 - sleva_poplatnik - 1267 - 1860)
    print(f"Čistá mzda je: {vypocet2} Kč")
else:("Něco se pokazilo, zkus to znovu.")

if dan == 15 and deti == 3:
    vypocet3 = vyplata - (socko + zdravko) - (superhruba * 0.15 - sleva_poplatnik - 1267 - 1860 - 2320)
    print(f"Čistá mzda je: {vypocet3} Kč")
else:("Něco se pokazilo, zkus to znovu.")

if vyplata >= 131901 and dan == 15:
    print("Máš větší příjem než 131 901Kč, tuďíš se na tebe vztahuje 23% daň.")

if vyplata <= 131901 and dan == 23:
    print("Máš menší příjem než 131 901Kč, tuďíš se na tebe vztahuje 15% daň.")