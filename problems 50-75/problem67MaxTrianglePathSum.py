file = open("p067_triangle.txt")
print(file.name)

data = []
for x in range(100):
    line = file.readline().rstrip("\n")
    l1 = line.split(" ")
    data.append(map(int,l1))


def processRow(l1, l2):
    for x in range(0,len(l1)):
        candidate1 = l2[x]
        candidate2 = l2[x+1]
        if candidate1 + l1[x] > candidate2 + l1[x]:
            l1[x] = candidate1+l1[x]
        else:
            l1[x] = candidate2+l1[x]
    return l1


x = len(data) - 2
while x >= 0:
    print(processRow(data[x],data[x+1]))
    x -= 1