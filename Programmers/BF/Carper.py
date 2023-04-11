def makePair(num):
    i=1
    pair = []
    while i < num/2+1:
        if num%i==0 and i >= num/i:
            pair+=[(i, int(num/i))]
        i+=1
    return pair


def solution(brown, yellow):
    pairs = makePair(brown+yellow)
    for i in pairs:
        w,h = i[0],i[1]
        while(h>0):
            if w * h == yellow : return [i[0],i[1]]
            else : w, h = w-2, h-2      


print(solution(10,2))