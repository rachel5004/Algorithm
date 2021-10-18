def solution(lst):
    dic = {}
    for i in lst:
        univ,drink = i.split()
        if univ in dic.keys(): dic[univ]+=int(drink)
        else: dic[univ]=int(drink)
    return max(dic,key=dic.get)

def test_case():
    assert solution(["Yonsei 10","Korea 10000000", "Ewha 20"])=="Korea"
    assert solution(["Yonsei 1", "Korea 10000000"])=="Korea"
