import sys
def solution():
    print(*sorted([int(sys.stdin.readline()) for _ in range(int(input()))], reverse = True))

# input()을 쓰면 시간 제한에서 걸림. 다른 sort를 쓴다면?