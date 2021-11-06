hooman = int(input("Enter the dog's age in human years: "))
doge = 0
for i in range(hooman + 1):
    if i <= 2:
        doge += 5.25
    else:
        doge += 4
print(f"The dog's age in dog’s years is {doge} years.")