from itertools import permutations

def solution(k, dungeons):
    result = 0
    for case in list(permutations(list(dungeons), len(dungeons))):
        cnt, hp = 0, k
        for i in case:
            if i[0] > hp: continue
            else : cnt, hp= cnt+1, hp-i[1]
        if cnt>result : result=cnt
    return result

print(solution(80, [[80,20],[50,40],[30,10]]))