from collections import deque
height,width,k = map(int, input().split())
field = [[0]*(width) for _ in range(height)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for m in range(x1, x2):
        for n in range(y1,y2):
            field[n][m] = 9

direction = [[1,0], [0,1],[-1,0], [0,-1]]
size = []
def bfs(y,x) :
    s = 1
    queue = deque()
    queue.append((x,y))
    field[y][x] = 1
    while (queue):
        prex, prey = queue.popleft()
        for d in direction:
            movex, movey = prex+d[0], prey+d[1]
            if 0<=movex<width and 0<=movey<height:
                if field[movey][movex] == 0:
                    queue.append((movex, movey))
                    field[movey][movex] = 1
                    s+=1
    size.append(s)


cnt=0

for i in range(width):
    for j in range(height):
        if field[j][i]==0:
            bfs(j,i)
            cnt+=1
size.sort()
print(cnt)
print(*size, sep=" ")