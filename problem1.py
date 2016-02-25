__author__ = 'matthew'

runningSum = 0
for x in range (1,1000,1):
    if x % 5 == 0:
        runningSum += x
    elif x % 3 == 0:
        runningSum += x

print(runningSum)


