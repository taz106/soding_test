def getDivisibleSum(num):
    total = 0
    for n in range(1, num):
        if (n%3 == 0) or (n%5 == 0):
            total += n
    return total

print(getDivisibleSum(1000))