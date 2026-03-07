num = int(input("Enter your number: "))
print("All even numbers untill 1 to ", num)
i = 1
while i <= num:
    if (i % 2) == 0:
        print(i)
    i += 1
