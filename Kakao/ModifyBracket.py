def divide(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(': cnt += 1
        else: cnt -= 1
        if cnt == 0: return p[:i + 1], p[i + 1:]

def solution(p):
    if not p: return ""
    u, v = divide(p)
    return u + solution(v) if u[0]=="(" else "("+solution(v)+")"+"".join(list("(" if i==")" else ")" for i in u[1:len(u) - 1]))