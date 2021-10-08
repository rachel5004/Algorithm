from itertools import permutations
def solution():
    num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for _ in range(int(input())):
        tmp,s,b = map(int, input().split())
        tmp = list(str(tmp))
        remove_cnt = 0

        for i in range(len(num)):
            s_cnt = b_cnt = 0
            i -= remove_cnt
            for j in range(3):
                tmp[j] = int(tmp[j])
                if tmp[j] in num[i]:
                    if j == num[i].index(tmp[j]): s_cnt+=1
                    else: b_cnt+=1
            if s_cnt!=s or b_cnt!=b:
                num.remove(num[i])
                remove_cnt += 1
    return len(num)

def test_case():
    assert 1


