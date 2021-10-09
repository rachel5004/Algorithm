def solution(idx,lst):
    return sorted(lst,reverse=True).index(lst[idx-1])+1

def test_case():
    assert solution(3,[[1,2,0],[0,1,0],[0,1,0],[0,0,1]]) == 2
    assert solution(2,[[3,0,0],[0,0,2],[0,2,0],[0,2,0]]) == 2

total,idx = map(int, input().split())
lst=[0]*total
for _ in range(total):
    i,g,s,b = map(int, input().split())
    lst[i-1]=[g,s,b]
print(sorted(lst,reverse=True).index(lst[idx-1])+1)