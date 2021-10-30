def solution(n,jump):
    res=[]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    matrix= [[0]*n for _ in range(n)]

    y, x, dir,cnt = 0, 0, 0, 1
    while True:
        if dir%2==0: target,another=y,x
        else:target,another=x,y

        if matrix[x][y] != 0: target+=1
        else:matrix[x][y] = cnt
        target += jump
        # 방향전환
        if target>n-1:
            another = (target-n)
            target=n-1
        if dir==0:
            y,x=target,another
        else:x,y=target,another
        dir = (dir + 1) % 4
        if cnt == 25: break
        cnt+=1
    return res

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def test_case():
    assert solution(5,3)==[5,2]