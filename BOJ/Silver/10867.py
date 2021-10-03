def solution(lst):
    return set(sorted(lst))

print(*solution([1,4,2,3,1,4,2,3,1,2]),sep=" ")

# solved
n=input()
lst=set(map(int,input().split()))
print(*sorted(lst),sep=" ")