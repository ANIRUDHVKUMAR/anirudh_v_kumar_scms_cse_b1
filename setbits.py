num = int(input("Enter the number"))
temp = num
bin=""
count=0
while(num>0):
    if num % 2 == 1:  
       count +=1
    num //=2
print("Set bits are :",count)