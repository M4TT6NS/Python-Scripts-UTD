import time
timer = int(input("How much seconds is your timer? "))
i = timer
while i >= 1:
    print(i)
    i -= 1
    time.sleep(1)
print("Timer is done!")
