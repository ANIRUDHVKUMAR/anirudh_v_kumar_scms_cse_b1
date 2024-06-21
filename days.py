day = int(input("Enter the Days: "))
year = day // 365
day -=year*365
weeks = day//7
day -= weeks*7
print(year," years, ",weeks," weeks, ",day," days") 