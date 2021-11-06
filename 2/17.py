x = int(input("x"))
y = int(input("y"))

if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x > 0 and y < 0:
    print("IV")
elif x == 0:
    print("the point is located on the y axis")
elif y == 0:
    print("the point is located on the x axis")
else:
    print("the point is located in the middle of the coordinate system")
        