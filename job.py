import time

text = input("PRESS ENTER TO START")


class stats:
    def __init__(self, vyrecnost, charisma, nasili):
        self.vyrecnost = vyrecnost
        self.charisma = charisma
        self.nasili = nasili

    def __str__(self):
        return f"Výřečnost: {self.vyrecnost}, Charisma: {self.charisma}, Násilí: {self.nasili}"

stats = stats(12, 8, 5)
print(stats)
print("Výřečnost slouží k přesvědčování")
print("Charisma slouží k ovlivňování")
print("Násilí slouží k zastrašování")

text = input("POKUD JSI READY STISKNI ENTER")
print("Jdi mladík, který má hádku se sousedem. Soused si stěžuje že rušíš noční klid, ale víš že je teprve 21:00. Pokus se situaci deeskalovat.")
time.sleep(2)
print ("Soused: Mám na tebe zavolat benga?")

hadka_1 = input("1 (výřečnost) 2 (charisma) 3 (násilí)")
if hadka_1 == "1":
    print("Otík: Je teprve 21:00, uklidni se. (ÚSPĚCH)")
    time.sleep(2)
    print("Soused: A co jako? Normální lidi vstávaj do práce!" )
    time.sleep(2)
    print("Otík: Já má taky práci takže co zkoušíš? (ÚSPĚCH) " )
    time.sleep(2)
    print("Soused se zamislel a odešel. " )


if hadka_1 == "2":
    print("Otík: Hele sousede, já vím že je pozdě, ale já se snažím si jenom užít večer.")
    time.sleep(2)
    print("Soused: A co já? Já mám taky nárok na klid!")
    time.sleep(2)
    print("Otík: No tak, sousede, vždyť mě znáš, já nejsem žádnej problémovej typ." )
    time.sleep(2)
    print("Soused ti to promine, ale je to na posled. (ÚSPĚCH)" )


if hadka_1 == "3":
    print("Otík: CHCEŠ ROZBÍT HUBU TY VOLE?! (NEÚSPĚCH)")
    time.sleep(2)
    print("Soused: MÁM ZAVOLAT BENGA?!")
    time.sleep(2)
    print("Otík: TAK ZAVOLEJ TY VOLE! (ÚSPĚCH)" )
    time.sleep(2)
    print("Soused: MÁM TAM NA TEBE VLÍTNOUT??" )
    time.sleep(2)
    print("Otík: TAK POĎ NE VOLE!! (NEÚSPĚCH)")
    time.sleep(2)
    print("Jelikož jsi byl opilý, nebyl jsi schopen porazit souseda a on ti rozbil hubu. (NEÚSPĚCH)")
