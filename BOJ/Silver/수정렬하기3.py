import sys

def solution():
    a = int(sys.stdin.readline())
    nums = [0]*a
    for i in range(a):
        nums[i]=int(sys.stdin.readline())
    nums.sort()
    print(*nums, sep="\n")


def solution2():
    nums = [0]*10001
    for _ in range(int(sys.stdin.readline())):
        nums[int(sys.stdin.readline())]+=1
    for i in range(1,10001):
        for _ in range(li[i]): print(i)

# solution2()
i=9
print(f"{i}\n"*2,end="")
li=[i for i in range(2, 5)]
for idx, i in enumerate(li):
    tmp = [idx for j in range(i)]
    print('\n'.join(map(str, tmp)))
    # print(*[idx for j in range(i)], sep="\n")