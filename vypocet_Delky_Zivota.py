age = int(input("Zadej, kolik je ti let. "))
remain = 80 - age
months = 12 * remain
weeks = 52 * remain
days = 365 * remain
print(f"Zbývá ti {days} dní, {weeks} týdnů nebo {months} měsíců a {remain} let do 80.")
