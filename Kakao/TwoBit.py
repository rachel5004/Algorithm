from math import ceil

def solution(numbers):
    answer = []
    for i in numbers:
        tmp = i
        n=0
        while(i>0):
            if i%2==0: break
            i=i//2
            n+=1
        answer.append(ceil(tmp + pow(2, n) - pow(2,n-1)))
        return answer

print(solution([2,7]))