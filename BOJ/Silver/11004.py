def solution(lst,idx):
    return sorted(lst)[idx-1]

def test_case():
    assert solution([4,1,2,3,5],2)==2
