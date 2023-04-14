def solution(n, left, right):
    res=[]
    for i in range(left, right+1):
        res.append(max(i//n,i%n)+1)
    return res

assert solution(4, 7, 14)==[4, 3, 3, 3, 4, 4, 4, 4]