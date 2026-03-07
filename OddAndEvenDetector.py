array = str(input("Enter your list array: "))  # 10 9 8 -9 10
lisst = array.split(" ")  # ["10", "9", "8", "-9", "10"]
evenNumbers = 0
oddNumbers = 0

for i in lisst:
    temp = int(i)
    if (temp % 2) == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1

print("Even Numbers: ", evenNumbers)
print("Odd Numbers: ", oddNumbers)
