def solution(n):
    cnt=0
    while n!=0:
        if n%2==1:
            cnt+=1
        n//=2
    return cnt

def test_case():
    assert solution(23)==4
    assert solution(32) == 1
    assert solution(64) == 1
    assert solution(48) == 2
    assert solution(1) == 1
