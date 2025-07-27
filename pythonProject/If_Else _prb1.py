# year = int(input("Enter a Year:"))
# if(year % 2 == 0 and (year % 100 != 0 or year % 400 == 0)):
   # print(f"{year} is a leap year.")
# else:
    # print(f"{year} is not a leap year.")

Number = int(input("Enter your Marks: "))
if(Number >= 90 and Number <=100):
    print(f"{Number} is A Grade")
elif(Number >= 80 and Number<=89):
    print(f"{Number} is B Grade")
elif(Number >= 70 and Number<=79):
    print(f"{Number} is C Grade")
elif(Number >= 60 and Number<=69):
    print(f"{Number} is D Grade")
else:
    print(f"{Number} is less than 60, Student Failed!")