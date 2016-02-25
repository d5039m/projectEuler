
x = 1
y = 1

i = 2
while len(str(y)) < 1000:
    c = x + y
    x = y
    y = c
    i+= 1

print i
