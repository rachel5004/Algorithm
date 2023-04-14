import sys
from collections import deque

input = sys.stdin.readline

node, edge, root = map(int, input().split())
graph = [[0] * (node+1) for _ in range(node + 1)]
dfs_visit = [0] * (node+1)
bfs_visit = [0] * (node+1)

for i in range(edge):
    fro, to = map(int, input().split())
    graph[fro][to] = graph[to][fro] = 1



def bfs(root):
    q = deque()
    q.append(root)
    bfs_visit[root] = 1
    while q:
        print("qhile~")
        root = q.popleft()
        print(root, end=" ")
        for i in range(1, node+1) :
            print("===== "+ str(i)+" =====")
            print(*[st for st in bfs_visit], sep=" ")
            print("=========")
            if bfs_visit[i] == 0 and graph[root][i] == 1 :
                q.append(i)
                bfs_visit[i] = 1
    


def print_matrix(matrix):
    for i in matrix:
        print('\t'.join(map(str, i)))


print_matrix(graph);

bfs(root)