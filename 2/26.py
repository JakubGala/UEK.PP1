pin = 2137
i = 0
while i <= 3:
    if int(input("Enter the PIN code: ")) == pin:
        print("najs")
        zdane = True
    else:
        print("incorrect")
    i += 1
    if i > 3:
        zdane = False
        
if zdane == False:
    print("karta zablokowana")