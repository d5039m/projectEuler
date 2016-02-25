

data = []

for x in range(2,531441):
    s = str(x)
    runningSum = 0
    for char in s:
       runningSum += int(char) ** 5
    if runningSum == x:
        data.append(x)

print sum(data)