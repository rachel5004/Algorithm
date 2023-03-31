from collections import deque
directions = [
    [0,1],[1,0],[-1,0],[0,-1]
]

n = int(input())

fields = [[0]*n for _ in range(n)]
cnt=0
homes = []
for i in range(n):
    fields[i] = list(map(int, list(input())))

def bfs(y, x):
    queue = deque()
    queue.append((x,y))
    fields[y][x] = 0
    home = 1;
    while(queue) :
        x,y = queue.popleft()
        for d in directions:
            move_x, move_y = x + d[0], y + d[1]
            if 0 <= move_x < n and 0 <= move_y < n:
                if fields[move_y][move_x]==1:
                    queue.append((move_x, move_y))
                    fields[move_y][move_x] = 0
                    home+=1
    homes.append(home)

for i in range(n):
    for j in range(n):
        if fields[j][i] == 1:
            bfs(j,i)
            cnt+=1

print(cnt)
homes.sort()
print(*homes, sep="\n")