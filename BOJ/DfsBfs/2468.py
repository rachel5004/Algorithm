from collections import deque

w = int(input())
direction = [[1,0],[0,1],[-1,0],[0,-1]]
# draw origin
origin = [[0]*w for _ in range(w)]
for i in range(w):
    origin[i] = list(map(int, input().split()))

res = 0
field= [[0]*w for _ in range(w)]

def make_field(limit):
    # check safe zone and caution zone
    for i in range(w):
        for j in range(w):
            if origin[i][j]<=limit: field[i][j]=0
            else : field[i][j]=1


def bfs(y,x) :
    global w
    queue = deque()
    queue.append((x,y))
    field[y][x] = 0
    while(queue):
        x,y = queue.popleft()
        for d in direction:
            movex, movey = x+d[0], y+d[1]
            if 0<=movex<w and 0<=movey<w:
                if field[movey][movex]==1:
                    queue.append((movex, movey))
                    field[movey][movex] = 0

for limit in range (max(map(max,origin))):
    make_field(limit)
    cnt=0
    for i in range(w):
        for j in range(w):
            if field[i][j]==1 :
                bfs(i,j)
                cnt+=1
    if cnt>res : res=cnt

print(res)