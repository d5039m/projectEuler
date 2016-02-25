sumSquares = 0
sum = 0
for x in xrange(1,101,1):
    sum += x
    sumSquares += pow(x,2)

squareSum = pow(sum,2)

diff = squareSum - sumSquares
print(diff)