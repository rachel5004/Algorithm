
from collections import defaultdict
from math import ceil

def solution(fees, records):
    tmp, res = defaultdict(int),defaultdict(int)
    for i in records:
        time, car, type = i.split(" ")
        h, m = map(int, time.split(":"))
        time = h*60+m
        if type=="IN": tmp[car] = time
        else: 
            res[car]+=(time-tmp[car])
            tmp[car]=-1
    print(tmp)
    print(res)
    for k,v in tmp.items():
        if v>=0 : res[k]+=(1439-v)

    answer = []
    for k,v in sorted(res.items()):
        overtime = v-fees[0]
        if overtime<=0 : answer.append(fees[1])
        else: answer.append(fees[1] + ceil(overtime/fees[2])*fees[3])
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))

