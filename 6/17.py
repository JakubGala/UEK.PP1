spam = [4,36,12,28,9,44,5]
eggs = [5,1,36]

for i in range(len(spam)):
    if spam[i] != eggs[0] and spam[i] != eggs[1] and spam[i] != eggs[2]:
        x = True
    else:
        x = False
    if x == True:
        print(spam[i])