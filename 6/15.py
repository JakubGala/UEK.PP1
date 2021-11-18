spam = ['blue', 'red', 'yellow']
with open('a.txt', 'w') as a:
    for i in spam:
        a.write(i)
        a.write("\n")