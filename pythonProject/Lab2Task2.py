def Abc():
    n2 = int(input("Enter how many values are in the list: "))
    list1 = []
    for i in range(n2):
        a = int(input("Enter value: "))
        list1.append(a)


    list1 = list(set(list1))


    list1.sort(reverse=True)

    print("Unique sorted list:", list1)


    list2 = []
    for b in list1:
        if b % 3 == 0:
            list2.append(b)

    return list2

print("The list of numbers divisible by 3 is:", Abc())
