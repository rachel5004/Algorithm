def solution(a,b,n,lst):
    num=0
    for i in range(n):
        num+=(a**i)*lst[len(lst)-i-1]
    res=[]
    while num:
        res.append(num % b)
        num //= b
    res.reverse()
    return res

def test_case():
    assert solution(17,8,2,[2,16])==[6,2]
