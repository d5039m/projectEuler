import math

value = math.factorial(100)
l1 = list(str(value))

sum = 0
for x in l1:
    sum += int(x)

print sum