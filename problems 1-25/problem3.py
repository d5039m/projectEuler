__author__ = 'matthew'

l1 = []

import math

def isPrime(x):
    if x % 2 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(x))),2):
        if x % i == 0:
            return False
    return True

def primeFactor(x):
    factors = []
    i = 2
    while i < math.sqrt(x):
        if x % i == 0:
            factors.append(i)
        i = i + 1

    print("Factors: " + str(factors))
    primes = []
    for value in factors:
        if isPrime(value):
            primes.append(value)

    return primes

primeFactors = primeFactor(600851475143)
print("Prime factors: "  + str(primeFactors))
print("Largest prime factor = " + str(max(primeFactors)))
