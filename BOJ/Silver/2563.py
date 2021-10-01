def solution(lst):
    matrix=[[0 for _ in range(101)] for _ in range(101)]
    # print_matrix(matrix)
    for x,y in lst:
        for i in range(x,x+10):
            for j in range(y,y+10):
                matrix[i][j] = 1
    answer = 0
    for row in matrix:
        answer += row.count(1)
    return answer

def test_case():
    assert solution([[3,7],[15,7],[5,2]])==260

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

