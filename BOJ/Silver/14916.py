def solution(n):
    if n in [1, 3]: return -1
    if (n%5)%2==1:
        return n//5-1+(n%5+5)//2
    else: return n//5+(n%5)//2

def test_case():
    assert solution(13)==5
    assert solution(14)==4