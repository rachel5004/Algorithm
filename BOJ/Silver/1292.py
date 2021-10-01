def solution(n,m):
    number=0
    for i in range(n,m+1):
        tmp=0
        while True:
            if sigma(tmp)<i<=sigma(tmp+1):
                number+=tmp+1;break
            tmp+=1
    return number

def sigma(n):
    return n*(n+1)/2

# with list
def solution2(n,m):
    num_list=[]
    for i in range(1,46):
        num_list.extend([i]*i)
        if len(num_list)>=m:break
    return sum(num_list[n-1:m])

def solution3(a,b):
    return sum(int(1+(8*n)**.5)//2 for n in range(a,b+1))

def test_case():
    assert solution(3,7)==15
    assert solution2(3, 7) == 15
    assert solution3(3, 7) == 15

# 시간은 2>3>1 순으로 빠름