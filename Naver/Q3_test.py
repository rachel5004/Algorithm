def solution(log):
    res=[]
    dic={}
    # dic={num:{q:score}}
    for i in log: #[수험번호, 문제번호, 점수]
        num,q,score = i.split()
        if num in dic.keys():
            dic[num][q] = score
        else:
            dic[num]= {q:score}
    for i in dic.keys():
        for j in dic.keys():
            if i!=j and len(dic[i])>=5 and len(dic[i])==len(dic[j]):
                for k in dic[i].keys():
                    if k in dic[j].keys():
                        if dic[i][k]==dic[j][k]:
                            res.append(i)
                            res.append(j)
    if res: return sorted(list(set(res)))
    else: return ["None"]
lst = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
lst2=["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]
def test_case():
    assert solution(lst)==["0001", "0002"]
    assert solution(lst2) == ["1101", "1102", "1901", "1902", "1903"]
    assert solution(["1901 10 50", "1909 10 50"]) == ["None"]

solution(lst2)