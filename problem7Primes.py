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
prime = 0
x = 2
while True:
    if isPrime(x):
        prime += 1
    if prime == 10001:
        print x
        break
    x += 1