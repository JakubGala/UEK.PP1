def spam(x, y):
    z = False
    for digit in x:
        if digit in y:
            z = True
        else:
            z = False
            break
    return z
arr1 = [1, 2, 3]
arr2 = [3, 2, 1, 4]
print(spam(arr1, arr2))
 
    