from collections import deque
res = []
directions = [
  [0,1], [1,0], [-1,0], [0,-1],
  [1,1],[-1,-1], [-1,1],[1,-1]
]
w,h = 0,0

def bfs(y, x):
    global w,h
    queue = deque()
    queue.append((x,y))
    fields[y][x] = 0
    while(queue) :
        x,y = queue.popleft()
        for d in directions:
            move_x, move_y = x + d[0], y + d[1]
            if 0 <= move_x < w and 0 <= move_y < h:
                if fields[move_y][move_x]==1:
                    queue.append((move_x, move_y))
                    fields[move_y][move_x] = 0   

while(True) :
    w,h = map(int, input().split())
    if w==0 and h ==0:
        break
    fields = []
    cnt=0
    for i in range(h):
        # fields[i] = list(map(int, input().split()))
        fields.append(list(map(int, input().split())))

    for i in range(h) :
        for j in range(w):
            if fields[i][j] == 1:
                bfs(i, j)
                cnt+=1
    res.append(cnt)          
print(*res, sep="\n")
