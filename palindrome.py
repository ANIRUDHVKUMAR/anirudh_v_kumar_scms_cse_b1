s = input("Enter the string: ")
i=0
flag=0
for ch in s[::-1]:
    print(ch)
    if ch == s[i]:
        i=i+1
    else:
        print("Not Palindrome")
        flag=1
        break
if(flag ==0):
    print("Palindrome")
    