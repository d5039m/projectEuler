#c >= 334
#b >= 334
#a <= 334

import math
c = 5
a = 1
b = 2

target = []
for a in xrange(1,335,1):
    for b in xrange(200,400,1):
        if a > b:
            continue
        for c in xrange(300,500,1):
            if a > c or b > c:
                continue
            else:
                if pow(a,2) + pow(b,2) == pow(c,2):
                    print "Triple: " + str(a) +" " + str(b) +" " +str(c)
                    if a + b + c == 1000:
                        target.append(a)
                        target.append(b)
                        target.append(c)


print target
product = 1
for x in target:
    product *= x
print product




