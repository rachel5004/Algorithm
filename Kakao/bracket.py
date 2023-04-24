def solution(s):
    start = {
        "{":"}",
        "(":")",
        "[":"]"
            }
    cnt=0
    for n in range(len(s)):
        s = s if n==0 else s[1:]+s[0]
        stack = []
        flag=True
        for i in list(s):
            if i in start: stack.append(i)
            elif not stack or i!=start[stack.pop()]: flag=False;continue;
        if not stack and flag: cnt+=1
    return cnt

# solved
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

    answer = []
    for q in query:
        q = q.replace('and ', '').split()

        pool = data[(q[0], q[1], q[2], q[3])]
        find = int(q[4])
        l,r,mid = 0,len(pool),0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:r = mid
            else: l = mid+1
        answer.append(len(pool)-l)
    return answer