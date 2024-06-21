def leap(year):
    if(year%4 == 0):
        if(year% 100 ==0):
            if(year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input("Enter the Year: "))
flag = leap(year)
if(flag):
    print("Leap year")
else:
    print("Not leap year")