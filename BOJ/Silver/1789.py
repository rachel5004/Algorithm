def solution(n):
    res=i=0
    while True:
        res+=i
        if res>n: return i-1
        i+=1


def test_case():
    assert solution(200)==19