attempts = 0

while attempts < 3:
    Color = input("Enter the Traffic Signal color (Red, Yellow, Green): ").lower()

    if Color == "red":
        print("Stop")
        break
    elif Color == "yellow":
        print("Slow down")
        break
    elif Color == "green":
        print("Gooooo")
        break
    else:
        print("Invalid Input")
        attempts += 1

if attempts == 3:
    print("Too many Invalid Inputs!,Exiting")
