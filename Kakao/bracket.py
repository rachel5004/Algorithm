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