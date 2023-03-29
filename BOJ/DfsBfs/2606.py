from collections import deque

n = int(input())
p = int(input())
graph = {}
for i in range(p) :
    s, t = map(int, input().split())
    if s in graph:
        graph[s].append(t)
    else:
        graph[s] = [t]
    if t in graph:
        graph[t].append(s)
    else:
        graph[t] = [s]

def bfs():


    queue = deque()
    queue.append(1)
    visited = [0] * (n+1)

    while(queue) :
        node = queue.popleft()
        visited[node]=1
        
        for i in graph[node] :
            if visited[i]==0:
                queue.append(i)
    print(sum(visited-1))

dfs_visited = [0]*(n+1)
def dfs(root):
    for i in graph[root]:
        if dfs_visited[i]==0:
            dfs_visited[i]=1
            dfs(i)

dfs(1)
print(sum(dfs_visited)-1)