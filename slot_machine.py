import random

print("🎰 Vítej v kasinovém automatu! 🎰")
print("💵 Jelikož jsi začátečník, tak ti dáme 1000 Kč do začátku. 💵\n")
zbytek = 1000
sloty = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]

while zbytek > 0:
    print(f"Aktuální zůstatek: {zbytek} Kč \n")
    castka = input("Kolik chceš vsadit? (nebo 'konec' pro ukončení): ")

    if castka.lower() == "konec":
        break

    if not castka.isdigit():
        print("❌ Neplatná částka. Zadej číslo.")
        continue

    castka = int(castka)

    if castka < 1:
        print("❌ Minimální sázka je 1 Kč.")
        continue
    if castka > zbytek:
        print("❌ Nemáš dostatek peněz!")
        continue

    zbytek = zbytek - castka
    vyherni_sloty = random.sample(sloty, 3)
    print("🎲 Výherní sloty:", vyherni_sloty)

    vyhra = 0

    if tuple(vyherni_sloty) == ("🍒", "🍒", "🍒"):
        vyhra = castka * 2
        print(f"Vyhrál jsi {vyhra}. Tvůj balanc je {zbytek + vyhra}.")
    elif tuple(vyherni_sloty) == ("🍋", "🍋", "🍋"):
        vyhra = castka * 2.5
        print(f"Vyhrál jsi {vyhra}. Tvůj balanc je {zbytek + vyhra}.")
    elif tuple(vyherni_sloty) == ("🔔", "🔔", "🔔"):
        vyhra = castka * 3
        print(f"Vyhrál jsi {vyhra}. Tvůj balanc je {zbytek + vyhra}.")
    elif tuple(vyherni_sloty) == ("⭐", "⭐", "⭐"):
        vyhra = castka * 3.5
        print(f"Vyhrál jsi {vyhra}. Tvůj balanc je {zbytek + vyhra}.")
    elif tuple(vyherni_sloty) == ("7️⃣", "7️⃣", "7️⃣"):
        vyhra = castka * 7
        print(f"Vyhrál jsi {vyhra}. Tvůj balanc je {zbytek + vyhra}.")
    else:
        print(f"\n😢 Bohužel, nic jsi nevyhrál. Tvůj balanc je {zbytek}.")

print(f"\n🎮 Hra ukončena. Zbývající zůstatek: {zbytek} Kč. Děkujeme za hru!")