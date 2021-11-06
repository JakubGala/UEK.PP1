kwota = int(input("Enter the amount in PLN: "))
print("5 zł – ", kwota // 5)
kwota = kwota % 5

print("2 zł – ", kwota // 2)
kwota = kwota % 2

print("1 zł – ", kwota // 1)
kwota = kwota % 1