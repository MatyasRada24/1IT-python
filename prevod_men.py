print("KURZY")
print(str("EU = 24.95Kč"))
print(str("GBP = 29.64Kč"))
print(str("RUB = 0.28Kč"))
print("!VÝSLEDKY SE ZAOKRUHUJÍ!")
print("---------------------------------------")
castka = float(input("Dobrý den, kolik peněz chcete převést? \n"))
mena = str(input("Dobrá, a o jakou měnu se jedná?  (CZK,EU,GBP,RUB) \n ")).upper()
mena2 = str(input("Výborně! A na jakou měnu chcete převést? (CZK,EU,GBP,RUB) \n ")).upper()

if mena == "CZK" and mena2 == "CZK":
    print("Víte, že převádíte české koruny. Že ano?")

if mena == "CZK" and mena2 == "EU":
    vypocet = round(castka * 0.04009)
    print(f"Dobře. Tady to máte: {vypocet} euro.")

if mena == "CZK" and mena2 == "GBP":
    vypocet2 =  round(castka * 0.03374)
    print(f"Dobře. Tady to máte: {vypocet2} liber.")

if mena == "CZK" and mena2 == "RUB":
    vypocet3 = round(castka * 3.593)
    print(f"Dobře. Tady to máte: {vypocet3} rublů.")

if mena == "EU" and mena2 == "CZK":
    vypocet4 = round(castka * 24.94)
    print(f"Dobře. Tady to máte: {vypocet4} korun.")

if mena == "EU" and mena2 == "EU":
    print("Víte, že převádíte euro. Že ano?")

if mena == "EU" and mena2 == "GBP":
    vypocet5 = round(castka * 0.8407)
    print(f"Dobře. Tady to máte: {vypocet5} liber.")

if mena == "EU" and mena2 == "RUB":
    vypocet6 = round(castka * 89.60)
    print(f"Dobře. Tady to máte: {vypocet6} rublů.")

if mena == "GBP" and mena2 == "CZK":
    vypocet7 = round(castka * 29.67)
    print(f"Dobře. Tady to máte: {vypocet7} korun.")

if mena == "GBP" and mena2 == "EU":
    vypocet8 = round(castka * 1.190)
    print(f"Dobře. Tady to máte: {vypocet8} euro.")

if mena == "GBP" and mena2 == "GBP":
    print("Víte, že převádíte libry. Že ano?")

if mena == "GBP" and mena2 == "RUB":
    vypocet9 = round(castka * 106,5)
    print(f"Dobře. Tady to máte: {vypocet9} rublů.")

if mena == "RUB" and mena2 == "CZK":
    vypocet10 = round(castka * 0.2785)
    print(f"Dobře. Tady to máte: {vypocet10} korun.")

if mena == "RUB" and mena2 == "EU":
    vypocet11 = round(castka * 0.01117)
    print(f"Dobře. Tady to máte: {vypocet11} euro.")

if mena == "RUB" and mena2 == "GBP":
    vypocet12 = round(castka * 0.009388)
    print(f"Dobře. Tady to máte: {vypocet12} liber.")

if mena == "RUB" and mena2 == "RUB":
    print("Víte, že převádíte rubl. Že ano?")

if mena != "CZK" and mena != "EU" and mena != "GBP" and mena != "RUB":
    print("Omlouvám se, ale takovou měnu neznám.")