year = int(input("enter the year to check : "))
if year%4==0 :
    if year%100==0 and year%400==0:
        print("it is a leap year")
    elif year%100==0:
        print("it is not")
    else:
        print("it is a leap year")
else:
    print("it is not")
