s = input("Enter the String")
s=s.lower()
print(s)
dict = {}
for ch in s:
    if ch.isalpha():
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
print(dict)