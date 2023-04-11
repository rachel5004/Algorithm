from itertools import permutations
import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: return False
    return True
def solution(numbers):
    cases = []
    for i in range(1, len(numbers)+1):
        cases+=[int(''.join(n)) for n in list(permutations(list(numbers), i))]
    cnt = 0
    for i in set(cases):
        if i>1 and isPrime(i) : cnt+=1
    return cnt
print(solution("011"))

