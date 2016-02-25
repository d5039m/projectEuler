
divisors = [11,12,13,14,15,16,17,18,19,20]

def check(x):
    for y in divisors:
        if x % y != 0:
            return False
    return True


x = 20
while True:
    found = check(x)
    if found:
        break
    else:
        x += 20

print(x)


