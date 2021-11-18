nums = [1,2,3]
x = 0
y = 0
for i in nums:
    if i > x:
        x = i
    if i < y:
        y = i
print(x, y)