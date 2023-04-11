from collections import defaultdict
from functools import reduce
def solution(clothes):
    type = defaultdict(int)
    for cloth in clothes:
        type[cloth[1]]+=1
    return reduce(lambda x, y: x * y, [i+1 for i in type.values()])-1
    

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


# from collections import Counter
# from functools import reduce
# def solution(clothes):
#     c = [a+1 for a in collections.Counter([x[1] for x in c]).values()]
#     answer = reduce(lambda x,y:x*y,c)-1
#     return answer
# reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1