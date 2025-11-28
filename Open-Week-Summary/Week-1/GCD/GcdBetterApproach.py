def gcd(x,y):
    (a,b) = max(x,y), min(x,y)
    if a%b == 0:
        return b
    else:
        return gcd(b,a-b)