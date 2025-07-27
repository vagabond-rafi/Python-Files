attempts = 0
while attempts < 3:
    salary = int(input("Enter Your Salary: "))
    if( salary>=5000 and salary <= 10000 ):
        print("You Do not have any Tax!")
        break
    elif(salary>10000 and salary<=50000):
        print(f"You Have 10% Tax and it is {salary*0.1}")
        break
    elif(salary>50000 and salary<=100000):
        print(f"You have 20% Tax and it is{salary*0.2}")
        break
    elif(salary>100000):
        print(f"You have 30% Tax and it is{salary*0.3}")
        break
    else:
        print("Invalid Input")
        attempts += 1
if attempts == 3:
    print("Too many Invalid inputs!,exiting")


