import math
def prime(n):
    flag,i = True,2
    while (flag == True and (i <= math.sqrt(n))):
        if(n%i) == 0:
            flag = False
            break
        i = i + 1
    return flag

print(prime(24))