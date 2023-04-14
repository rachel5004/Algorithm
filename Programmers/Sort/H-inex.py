from collections import Counter
def solution(citations):
    citations.sort()
    # 0 3 5 5 6
    for i in citations:
        if len(citations[citations.index(i):]) > citations[:citations.index(i)+1][-1]:
            return i
    return citations[-1]
print(solution([3, 0, 6, 5, 5]))