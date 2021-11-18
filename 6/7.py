nums = [1,2,4,2,0,7,3,5]
odd = 0
even = 0
for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
        
print(f"odd: {odd} even: {even}")