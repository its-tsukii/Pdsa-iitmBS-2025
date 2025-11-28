def factors(n):
    f1 = []
    for i in range(1,n+1):
        if n % i == 0 :
            f1.append(i)
    return f1

def prime(n):
    return (factors(n) == [1,n])

print(prime(13))