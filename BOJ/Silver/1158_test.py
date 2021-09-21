def solution(n,k):
    lst = [i for i in range(1,n+1)]
    res=[]
    idx = 0
    while len(lst) > 0:
        idx = (idx+k-1)%len(lst)
        res.append(lst.pop(idx))
    return res

def test_case():
    assert solution(7,3)==[3, 6, 2, 7, 5, 1, 4]

n,k = map(int,input().split())
print("<%s>" % (", ".join(map(str,solution(n,k)))))