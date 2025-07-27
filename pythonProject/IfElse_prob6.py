n1 = int(input("Enter the 1st Number:"))
n2 = int(input("Enter the 2nd Number:"))
n3 = int(input("Enter the 3rd Number:"))

if( n1>n2 and n1>n3) :
    print("Number One Largest")
elif( n2>n1 and n2>n3) :
    print("Number Two Largest")
else:
    print("Number Three Largest")

if( n1<n2 and n1<n3) :
    print("Number One Smallest")
elif( n2<n1 and n2<n3) :
    print("Number Two Smallest")
else:
    print("Number Three Smallest")

if (n1>n2 and n1<n3) or (n1>n3 and n1<n2):
    print("Number One is the Middle")
elif(n2<n1 and n2>n3) or (n2>n1 and n2<n3):
    print("Number Two is the Middle")
else:
    print("Number Three is the Middle ")

