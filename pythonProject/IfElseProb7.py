hour = int(input("Enter the hour in 24 hour format(0-23): "))

if 0<= hour <= 23 :
    if hour == 0:
        print("Midnight")
    elif 1 <= hour < 12:
        print(f"{hour} AM")
    elif hour == 12:
        print("12 PM")  # Noon
    else:
        print(f"{hour - 12} PM")
else:
    print("Invalid Input")

