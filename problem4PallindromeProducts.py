

def pallindrome(l1):
    i = 0
    j = len(l1) - 1

    if len(l1) % 2 == 0:
        while i < j:
            if l1[i] != l1[j]:
               return False
            i += 1
            j -= 1
    else:
        while  j - i > 1:
            if l1[i] != l1[j]:
               return False
            i += 1
            j -= 1

    return True

iter = 1
x = 999
y = 999
found = False

pallindromes = []
while x > 1:
    while y > 1:

        test = x * y
        if pallindrome(list(str(test))):
            pallindromes.append(test)
        y -= 1
    x -= 1
    y = 999

print(max(pallindromes))



