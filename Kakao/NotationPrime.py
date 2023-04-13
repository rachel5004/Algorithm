from math import sqrt
def toDecimal(num, k) :
    d = ""
    while(num//k>0):
        d, num= str(num%k)+d, num//k
    return str(num)+d
def isPrime(n):
    if n==1 : return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0: return False
    return True
def solution(n, k):
    cnt=0
    for i in list(map(int, filter(len, toDecimal(n,k).split("0")))):
        if isPrime(i)==True: cnt+=1
    return cnt

print(solution(110011,10))
