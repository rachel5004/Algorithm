n=int(input().split())
for j in range(len(n)):
    for i in range(1, len(n)):
        if n[i]<n[j-1]:
            n[i],n[j-1]=n[i-1],n[j]
            print(''.join(n))