def solution(e,s,m):
    answer = 1
    while True:
        if answer % 15 == e % 15 and answer % 28 == s % 28 and answer % 19 == m % 19:
            return answer
        answer+=1


# e,s,m = map(int,input().split())
# print(solution(e,s,m))

def sol(e,s,m):
    return [i for i in range(s, 7981, 28) if i % 15 == e % 15 and i % 28 == s % 28 and i % 19 == m % 19][0]



def test_case():
    # assert solution(1,16,16) == 16
    # assert solution(1,2,3) == 5266
    # assert solution(15,28,19) == 7980
    for i in range(1, 16):
        for j in range(1, 29):
            for k in range(1, 20):
                assert solution(i, j, k) == sol(i, j, k)