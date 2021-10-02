def solution(lst1,lst2):
    return sorted(lst1+lst2)

# def test_case():
#     assert solution([2,9],[3,5])==[2,3,5,9]
#     assert solution([1], [4, 7]) == [1,4,7]
#     assert solution([1,4,7],[2,3,5,9]) == [1,2,3,4,5,7,9]

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*sorted(a+b),sep=" ")

