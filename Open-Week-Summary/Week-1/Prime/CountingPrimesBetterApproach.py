def prime(n):
    flag = True
    for i in range(2, n//2):
        if(n%i) == 0:
            flag = False
            break
    return flag

print(prime(24))