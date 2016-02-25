import math

def isPrime(x):
    if x == 2:
        return True
    elif x == 1:
        return False
    elif x % 2 == 0:
        return False
    else:
        for y in range(3,int(math.sqrt(x))+1,2):
            if x % y == 0:
                return False
        return True
sum = 2
for x in range(1,2000001,2):
    print x
    if isPrime(x):
        sum += x

print sum

