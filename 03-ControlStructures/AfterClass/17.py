x = int(input("enter x: "))
y = int(input("enter y: "))

if x == 0 and y == 0 :
    print(f"Point P({x},{y}) is in the start of the coordinate system")
elif x >0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x <0 and y > 0 :
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x <0 and y<0 :
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
elif x > 0 and y<0:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
elif x ==0 and y >0 :
    print(f"Point P({x},{y}) is in beetwen the first and second quadrant of the coordinate system")
elif x ==0 and y < 0 :
    print(f"Point P({x},{y}) is in beetwen the third and fourth quadrant of the coordinate system")
elif x > 0 and y == 0 :
    print(f"Point P({x},{y}) is in beetwen the first and fourth quadrant of the coordinate system")
else:
    print(f"Point P({x},{y}) is in beetwen the second and third quadrant of the coordinate system")
