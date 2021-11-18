eggs = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
x = ''
for i in eggs:
    if len(i) > len(x):
        x = i
print(x)