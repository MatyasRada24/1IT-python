right_answers = ["Harry Potter", "Albus Brumbál", "Sirius Black", "Severus Snape"]
user_answers = []
questions = [
    "Jak se jmenuje hlavní hrdina v Harry Pottrovy?",
    "Jak se jmenuje ředitel Bradavic?",
    "Jak se jmenuje kmotr Harryho Pottera?",
    "Jak se jmenuje kouzelník, který vymyslel zaklínadlo Sectumsempra?"
]

# Získání odpovědí od uživatele
for question in questions:
    answer = input(question + " ")
    user_answers.append(answer)

# Porovnání odpovědí a výpočet úspěšnosti
correct_count = 0
for i in range(len(right_answers)):
    if user_answers[i].strip().lower() == right_answers[i].strip().lower():
        correct_count += 1

# Výpočet procentuální úspěšnosti
success_rate = (correct_count / len(right_answers)) * 100

print(f"Vaše úspěšnost je {success_rate:.2f}%")
