from collections import deque
directions = [
  [0,1], [1,0], [-1,0], [0,-1]
]
pos_x, pos_y = 0,0

def dfs(x, y) :
    pos[x][y] = 0
    for d in directions:
       # 다음에 이동하는 좌표
        move_x, move_y = x + d[0], y + d[1]
        # 이동 가능한 좌표이면
        if 0 <= move_x < pos_x and 0 <= move_y < pos_y:
            if pos[move_x][move_y]:
                dfs(move_x, move_y)  

def bfs(x, y) :
    queue = deque()
    queue.append((x,y))
    pos[x][y] = 0

    while(queue):
        x,y = queue.popleft()
        for d in directions:
        # 다음에 이동하는 좌표
            move_x, move_y = x + d[0], y + d[1]
            # 이동 가능한 좌표이면
            if 0 <= move_x < pos_x and 0 <= move_y < pos_y:
                if pos[move_x][move_y]==1:
                    queue.append((move_x, move_y))
                    pos[move_x][move_y] = 0   

for _ in range(int(input())) :
    pos_x, pos_y, n = map(int, input().split())
    pos = [[0]*pos_y for _ in range(pos_x)]
    cnt = 0
    for _ in range(n):
        x ,y  =  map(int, input().split())
        pos[x][y] = 1

    # for i in range(pos_x) :
    #     for j in range(pos_y):
    #         if pos[i][j] == 1:
    #             dfs(i,j)
    #             cnt+=1
   
    for i in range(pos_x) :
        for j in range(pos_y):
            if pos[i][j] == 1:
                bfs(i,j)
                cnt+=1
    print(cnt)

