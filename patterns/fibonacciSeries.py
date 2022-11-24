n1 = 0
n2 = 1
sumPrevious = 0
last = int(input("Enter last term: "))
while (n1 + n2) < last:
    sumPrevious = n1 + n2
    print(sumPrevious, end=", ")
    n1 = n2
    n2 = sumPrevious
