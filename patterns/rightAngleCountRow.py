a = int(input("How many terms: "))
for i in range(0, a):
    for j in range(1, (a-1)%2):
        print(" ", sep="", end="")
        for k in range(1, a):
            print("*", sep="", end="")
    print("")