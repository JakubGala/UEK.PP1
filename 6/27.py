eggs = [5,4,3,2,6,5]
def spam(x):
    print(*x, sep=',')
    
spam(eggs)