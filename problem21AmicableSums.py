import math

cache = {}

def getFactors(x):
    factors = [1]
    i = 2
    while i <= x // 2:
        if x % i == 0:
            factors.append(i)
        i = i + 1

    return factors

amicable = []
for x in range(220,15000,1):
    if x in cache:
        factors = cache[x]
    else:
        factors = getFactors(x)
        cache[x] = factors

    sumOfFactors = sum(factors)

    if sumOfFactors in cache:
        testFactors = cache[sumOfFactors]
    else:
        testFactors = getFactors(sumOfFactors)
        cache[sumOfFactors] = testFactors

    sumOfTestFactors = sum(testFactors)

    if x == sumOfTestFactors and x != sumOfFactors and x < 10000 and sumOfFactors < 10000:
        if x not in amicable:
            amicable.append(x)
        if sumOfFactors not in amicable:
            amicable.append(sumOfFactors)


print amicable
print sum(amicable)