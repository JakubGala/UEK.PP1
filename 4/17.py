spam = "You never get a second chance to make a first impression"
def letter(x):
    z = 0
    for i in spam:
        if i == x:
            z += 1
    print(z)
letter('e')


        