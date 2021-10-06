def solution():
    lst = [int(input()) for _ in [0] * 8]
    res =sorted(lst)[3:]
    print(sum(res))
    print(*sorted([lst.index(x)+1 for x in res]))

def test_case():
    assert solution([20,30,50,48,33,66,0,64])==[261,[3,4,5,6,8]]
    assert solution([20,0,50,80,77,110,56,48]) == [373, [3,4,5,6,7]]
