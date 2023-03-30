from collections import deque

n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
cnt = 0;

for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(n):
    queue = deque()
    queue.append(n)
    while(queue):
        no = queue.popleft()
        for i in graph[no]:
            if visited[i]==0:
                visited[i] = 1
                queue.append(i)

for i in range(1,n+1) :
    if visited[i]==0:
        bfs(i)
        cnt+=1
print(cnt)