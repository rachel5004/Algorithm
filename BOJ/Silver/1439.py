# with string slicing
def solution(s):
    zero,one=0,0
    while s!="":
        if s[0]=="0":
            zero += 1
            s=s[s.find("1"):] if s.find("1")!=-1 else ""
        else:
            one += 1
            s=s[s.find("0"):] if s.find("0")!=-1 else ""
    return min(zero,one)

# with char change
def solution2(s):
    count=0
    for i in range(len(s) - 1):
        if s[i]!=s[i+1]: count+=1
    return (count+1)//2
def solution2_2(s):
    return (s.count("01")+s.count("10")+1)//2

def solution3(s):
    from itertools import groupby
    return len([*groupby(s)])//2

def test_case():
    assert solution2_2("0001100")==1
    assert solution2_2("110001100")==2
    assert solution2_2("1101001100") == 3
