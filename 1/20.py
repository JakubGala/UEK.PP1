weight = float(input("waga:"))
height = float(input("wzrost w metrach:"))
BMI = weight / height ** 2
if BMI <= 24.9 and BMI >= 18.5:
    print("Prawidlowe BMI")
elif BMI < 18.5:
    print("Niedowaga")
else:
    print("Nadwaga")
