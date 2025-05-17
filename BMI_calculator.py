mass = input("Napiš svojí hmotnost v kg: ")
height = input("Napiš svou výšku v metrech: ")
BMI = float(mass) / float(height)**2

if BMI < 18.5:
    print(f"Tvoje BMI je {BMI:.2f}, máš podváhu.")
elif 18.5 <= BMI <= 25:
    print(f"Tvoje BMI je {BMI:.2f}, máš normální váhu.")
else:  # tedy BMI > 25
    print(f"Tvoje BMI je {BMI:.2f}, máš nadváhu.")
