side1 = int(input("Enter the 1st Number:"))
side2 = int(input("Enter the 2nd Number:"))
side3 = int(input("Enter the 3rd Number:"))

if (side1+side2>side3 and side1+side3>side2 and side2+side3>side1):
    if side1 == side2 == side3:
        print("Equilateral triangle")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

else:
    print("Invalid triangle - the sides do not satisfy triangle inequality.")

