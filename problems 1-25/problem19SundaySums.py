nonLeap = [1,32,60,91,121,152,182,213,244,274,305,335]
leapFirsts = [1,32,61,92,122,153,183,214,245,275,306,336]

def isLeapYear(year):
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        elif year % 4 == 0:
            return True
        else:
            return False


day = 6
year = 1901
sundayFirst = 0
while year < 2001:
    leap = isLeapYear(year)
    if leap:
        if day in leapFirsts:
            sundayFirst += 1
    else:
        if day in nonLeap:
            sundayFirst += 1

    day += 7
    if leap:
        if day > 366:
            day = day % 366
            year += 1
    else:
        if day > 365:
            day = day % 365
            year += 1

print sundayFirst
