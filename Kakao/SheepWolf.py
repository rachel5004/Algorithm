from collections import defaultdict
# fail
def solution2(info, edges):
    map = defaultdict(list)
    for i in edges: map[i[0]].append(i[1])

    maxsheep, sheep, wolf = 0,0,0
    visited = [0]*len(info)
    def dfs(num):
        nonlocal sheep, wolf, maxsheep
        if info[num]==0: sheep+=1
        else: wolf+=1
        if wolf>=sheep : return
        else: 
            maxsheep = max(sheep, maxsheep)
            for i in map[num]:
                if visited[i]==0:
                    visited[i]==1
                    dfs(i)
                    visited[i]=0
                    visited[num]=1
    visited[0]=1
    dfs(0)
    return sheep

def solution(info, edges):
    visited = [0] * len(info)
    maxsheep = 0
    def dfs(sheep, wolf):
        nonlocal maxsheep
        if sheep > wolf : maxsheep = max(maxsheep, sheep)
        else : return 
        for i in edges:
            if visited[i[0]] and not visited[i[1]]:
                visited[i[1]] = 1
                if info[i[1]] == 0: dfs(sheep+1, wolf)
                else: dfs(sheep, wolf+1)
                visited[i[1]] = 0

    visited[0] = 1
    dfs(1, 0)
    return maxsheep

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution2([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))