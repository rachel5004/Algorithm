def solution(board, skill):
    cnt=0
    for type, r1, c1, r2, c2, degree in skill:
        cnt=0
        if type == 1: degree = -degree
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                board[i][j]+=degree
    for i in board:
        for j in i:
            if j>0:cnt+=1
    return cnt