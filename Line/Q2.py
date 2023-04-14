def solution(r,c):
    matrix= [[0]*c]*r

    dx=[0,1,0,-1]
    dy=[-1,0,1,0]
    cnt=1
    dir = 0    #0,2는 좌우 1,3은 상하
    x,y=0,c
    while cnt<=r*c:
        for _ in range(1,c if dir%2==0 else r):
            x+=dx[dir]; y+=dy[dir]
            matrix[x][y] = cnt
            cnt+=1
            print_matrix(matrix)
        dir=(dir+1)%4
        if dir%2==1: r-=1
        else: c-=1

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

solution(5,4)