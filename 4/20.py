def power(x, y):
    if y == 1:
        return x
    x = x * power(x, y - 1)
    return x

print(power(2, 5))