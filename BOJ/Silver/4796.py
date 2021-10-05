def solution(l,p,v):
    res=(v//p)*l + (l if v%p>l else v%p)
    return res
def test_case():
    assert solution(5,8,20) == 14
    assert solution(5, 8, 17) == 11

i=0
while True:
    i+=1
    l,p,v = map(int,input().split())
    if l == p == v ==0: break
    print(f"Case {i}: {solution(l,p,v)}")