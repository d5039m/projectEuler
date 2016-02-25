sum = 0
for x in range(1,1001):
    y = x ** x
    sum += y

print sum

l1 = list(str(sum))
print "".join(l1[-10:])

