from collections import deque
n = int(input())
tree = list(map(int, input().split()))
graph = {}
cnt=0
for i in range(n+1):
    graph[i]=[]
for i in range(len(tree)):
    parent = tree[i]
    if parent == -1 : continue  
    else: graph[parent].append(i)
def dfs(root):
    global cnt
    for i in graph[root]:
        # 다음 방문 노드가 remove인지 확인하고, 맞다면 continue
        if i == remove:
            if len(graph[root]) == 1:
                cnt+=1
            continue
        if not graph[i]: 
            cnt+=1
            continue
        dfs(i)
remove = int(input())
if remove==tree.index(-1): print(0)
else : 
    dfs(tree.index(-1))
    print(cnt)