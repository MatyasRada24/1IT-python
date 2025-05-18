import random

tajne_cislo = random.randint(1, 10)
hadani = int(input("Hádej číslo od 1 do 10: "))

if hadani == tajne_cislo:
    print("Správně! Uhodl jsi číslo.")
else:
    print("Špatně, správné číslo bylo", tajne_cislo)
