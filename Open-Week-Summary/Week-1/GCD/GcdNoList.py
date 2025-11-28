def gcd(x,y):
    for i in range(1,min(x,y)+1):
        if x % i == 0 and y % i == 0 :
            res = i
    return res

print(gcd(4,12))

# gcd means a number that can divide both the x and y and not leave any remainder that is both x,y % n == 0