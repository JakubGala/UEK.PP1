array = [15, 38, 7, 23, 14]
def spam(z):
    x = False
    for i in range(len(array)):
        if array[i] == z:
            x = True
    if x == True:
        print(f"{z} appears in the array")
    else:
        print(f"{z} does not appear in the array")
spam(16)