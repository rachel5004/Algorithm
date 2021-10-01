def solution(n):
    lst=sorted(list(str(n)),reverse=True)
    if lst[-1]!="0" or sum(list(map(int,lst[:-1])))%3!=0: return -1
    return int(''.join(lst))

def test_case():
    assert solution(30)==30
    assert solution(2931) == -1
    assert solution(102) == 210
    assert solution(80875542) == 88755420