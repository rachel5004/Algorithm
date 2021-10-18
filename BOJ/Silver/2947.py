n=input().split()
def sort(n):
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]
            print(' '.join(n))
while[*"12345"]<n: sort(n)
