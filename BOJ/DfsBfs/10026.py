from collections import deque
direction = [[0,1],[1,0],[0,-1],[-1,0]]
n = int(input())

field = [[0]*n for _ in range(n)]
rg_field =[[0]*n for _ in range(n)]
for i in range(n):
    value = list(list(input()))
    field[i] = value
    rg_field[i]= ["R" if v == "G" else v for v in value]

def bfs(y,x,color):
    global n
    queue = deque()
    queue.append((x,y))
    field[y][x]="D"
    while (queue):
        x,y = queue.popleft()
        print(str(x)+" "+str(y))
        for d in direction:
            movex, movey = x+d[0], y+d[1]
            if 0<=movex<n and 0<=movey<n:
                if field[movey][movex] == color:
                    queue.append((movex,movey))
                    field[movey][movex]="D"
cnt = 0
for i in range(n):
    for j in range(n):
        if field[i][j]!="D":
            color = field[i][j]
            bfs(i, j, color)
            cnt+=1

field = rg_field
rg_cnt = 0
for i in range(n):
    for j in range(n):
        if field[i][j]!="D":
            color = field[i][j]
            bfs(i,j, color)
            rg_cnt+=1

print(str(cnt)+" "+str(rg_cnt))