n1 = int(input("Enter a number: "))

if n1 < 0:
    print("Invalid input")
else:
    f = 1
    for i in range(1, n1 + 1):
        f *= i
    print(f"Factorial of {n1} is {f}")