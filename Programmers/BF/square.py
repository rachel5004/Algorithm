def solution(sizes):
    maxv = 0
    minv=0
    for i in sizes:
        if max(i) > maxv: maxv = max(i)
        if min(i) > minv: minv = min(i)
    return max(max(i) for i in sizes)*max(min(i) for i in sizes)


print(solution([[10, 7], [12, 3], [5, 15], [14, 7], [8, 15]]))