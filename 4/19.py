def spam(z, x, y):
    if z > x and z < y:
        return True
    else:
        return False
    
print(spam(20, 10, 100))