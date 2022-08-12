def is_leap(year):
    leap1=True
    leap = False
    if (year%4)==0 and (year%100)!=0:
       return leap1
    elif (year%100)==0 and (year%400)==0:
        return leap1
    else:
       return leap

year = int(input())
print(is_leap(year))

