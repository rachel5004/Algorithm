import math

def solution(n,m):
    gcd=lcm=1
    n,m=min(n,m),max(n,m)
    if m%n==0: return [n,m]
    for i in range(2, int(math.sqrt(m)) + 1):
        while True:
            if n % i == 0 and m % i == 0:
                gcd *= i
                n, m = n // i, m // i
            else: break
    lcm=gcd*n*m
    return [gcd,lcm]

def Euclidean_gcd(n,m):
    while m: n,m=m,n%m
    return n
def Euclidean_lcm(n,m):
    return (n*m)//Euclidean_gcd(n,m)

def test_case():
    # with math module
    assert math.gcd(24,18) == 6
    assert math.lcm(24, 18) == 72
    # with Euclidean algorithm
    assert Euclidean_gcd(24,18)==6
    assert Euclidean_lcm(24,18) == 72
    # with solution
    n,m=373,742
    assert solution(n,m)==[math.gcd(n, m),math.lcm(n,m)]