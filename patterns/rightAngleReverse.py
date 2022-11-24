n = int(input("How many rows of reverse triangle pattern you want: "))
for i in range(0, n):
    for j in range(0, n - i):
        print("*", end=" ")
    print("")