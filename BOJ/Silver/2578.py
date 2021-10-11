matrix = [[0 for _ in range(5)] for _ in range(5)]
for i, v in enumerate(
        [[11,12,2,24,10], [16,1,13,3,25], [6,20,5,21,17], [19,4,8,14,9], [22,15,7,23,18]]):
    for j in range(5): matrix[i][j] = v[j]
cnt,bingo = 0,[]
reversed_matrix = [list(x) for x in zip(*matrix)]
# reversed_matrix=list(map(list, zip(*matrix)))

def print_matrix(matrix):
    for i in matrix:
        print('\t'.join(map(str, i)))

# solution
bingo = [list(map(int, input().split())) for _ in range(5)]
targets = []
for _ in range(5): targets.extend(list(map(int, input().split())))

visitied = [[False] * 5 for _ in range(5)]
row_visited,col_visited,x_visited= [False]*5,[False]*5,[False]*2

def is_bingo():
    for i in range(5):
        if all(visitied[i]): row_visited[i] = True

    for i in range(5):
        temp = []
        for j in range(5): temp.append(visitied[j][i])
        if all(temp): col_visited[i] = True

    temp_up,temp_down = [],[]
    for i in range(5):
        temp_up.append(visitied[i][i])
        temp_down.append(visitied[i][4 - i])
    if all(temp_down): x_visited[0] = True
    if all(temp_up): x_visited[1] = True

def count_bingo():
    count = 0
    for i in range(5):
        if row_visited[i]: count += 1
        if col_visited[i]: count += 1
    for i in x_visited:
        if i: count += 1
    return count

for j in range(len(targets)):
    x = None
    for i in range(5):
        if targets[j] in bingo[i]:
            x = i
            break
    y = bingo[x].index(targets[j])

    visitied[x][y] = True
    is_bingo()
    if count_bingo() >= 3:
        print(j + 1)
        break