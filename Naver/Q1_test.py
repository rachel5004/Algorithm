def solution(lst,k):
    res=0
    dic = {}
    for i in lst:
        tmp = list(set(i.split()))
        for j in tmp:
            if j in dic.keys(): dic[j]+=1
            else: dic[j]=1
    for i in dic.values():
        if i>k:i=k
        res+=i
    return res

def test_case():
    assert solution(["A B C D", "A D", "A B D", "B D"],2)==7
    assert solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3) == 8
