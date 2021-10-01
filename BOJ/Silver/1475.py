def solution(n):
    lst = [0] * 10
    for i in n:
        if (i == '6' or i == '9'):
            lst[6]+=1
        else:
            lst[int(i)] += 1
    lst[6] = lst[6]//2 if (lst[6]%2==0) else lst[6]//2+1
    return max(lst)

def test_case():
    assert solution("9999")==2
    assert solution("1234") == 1
    assert solution("1111") == 4
