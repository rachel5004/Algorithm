def solution():
    # i = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    return lst[0]*lst[-1]
# print(solution())