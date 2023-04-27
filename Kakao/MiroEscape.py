from itertools import product

def solution(n, m, x, y, r, c, k):
    move = {"d":[1,0],
            "l":[0,-1],
            "r":[0,1],
            "u":[-1,0]}
    if k-(abs(x-r)+abs(y-c))%2==1: return 'impossible'
    for case in sorted(product(move.keys(), repeat=k)):
        sx, sy, flag = x, y, True
        for i in case:
            movex, movey = sx+move[i][0], sy+move[i][1]
            if not (0<movex<=n and 0<movey<=m): flag=False;break
            sx,sy = movex, movey
        if flag and sx==r and sy==c: return ''.join(case)
    return 'impossible'


def solution(n, m, x, y, r, c, k):
    gap= abs(x-r)+abs(y-c)
    if gap%2!=k%2 or gap>k: return 'impossible'

    k,d,l,rr,u = k-gap,0,0,0,0
    if x<r : d = r-x
    else: u = x-r
    if y<c : rr = c-y
    else: l = y-c

    dplus = min(n-max(x,r), k//2)
    k -= dplus*2

    lplus = min(min(y,c)-1, k//2)
    k -= lplus*2

    return 'd'*(d+dplus)+'l'*(l+lplus)+'rl'*(k//2)+'r'*(rr+lplus)+'u'*(u+dplus)
print(solution(3, 4, 2, 3, 3, 1, 5))
