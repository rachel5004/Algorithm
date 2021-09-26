import math

def fac(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    return res
def sol(n,m):
    return fac(m)/(fac(m-n)*fac(n))

def solution():
    answer = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        answer.append(math.factorial(m)/(math.factorial(m-n)*math.factorial(n)))
    print(*answer, sep="\n")

def test_case():
    assert sol(1,5) == 5
    assert sol(13,29)==67863915
