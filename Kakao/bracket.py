def solution(s):
    start = {
        "{":"}",
        "(":")",
        "[":"]"
            }

    cnt=0
    for n in range(len(s)):
        tmp = s if n==0 else s[n:]+s[:n-1]
        stack = []
        flag=True
        for i in list(tmp):
            if i in start: stack.append(i)
            elif not stack or i!=start[stack.pop()]: flag=False;continue;
        if flag: cnt+=1
    return cnt