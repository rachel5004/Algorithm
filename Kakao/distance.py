def solution(places):
    answer, distance = [], [[1,0], [0,-1], [-1,0], [0,1]]
    for place in places:
        res, field = 1, [list(i) for i in place]
        for i in range(5):
            for j in range(5):
                if field[i][j] =='P':
                    if i+1<5 and field[i+1][j]=='P': res=0;break;
                    if j+1<5 and field[i][j+1]=='P': res=0;break;
                if field[i][j] =='O':
                    p_cnt=0
                    for d in distance:
                        if 0<=i+d[0]<5 and 0<=j+d[1]<5 and field[i+d[0]][j+d[1]]=='P': p_cnt+=1
                        if p_cnt==2 : res=0;break;
        answer.append(res)
    return answer

print(solution([["POPOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))