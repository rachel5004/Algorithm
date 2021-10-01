def solution():
    s = [0]*20
    idx=0
    for _ in range(int(input())):
        command = input()
        if command=="all":
            for i in range(0,20): s[i]=i+1
        elif command=="empty":
            for i in range(0,20): s[i]=0
        else:
            command, number = command.split()
            d = {'add' : add,'remove':remove, 'check':check,'toggle':toggle}
            d[command](s,int(number))

ans=[]
idx=0
def solution2(lst):
    s = [0]*21
    for l in lst:
        command = l
        if command=="all":
            for i in range(0,20): s[i]=i+1
        elif command=="empty":
            for i in range(0,len(s)): s[i]=0
        else:
            command, number = command.split()
            d = {'add' : add,'remove':remove, 'check':check,'toggle':toggle}
            d[command](s,int(number))
    return ans

def add(s,number):
    global idx
    s[idx]=number
    idx+=1

def remove(s,number):
    del s[s.index(number)]
    global idx
    idx-=1

def check(s,number):
    global ans
    res=0
    if s.count(number): res=1
    ans.append(res)
    return res

def toggle(s,number):
    if check(s,number): remove(s,number)
    else: add(s,number)


command = ["add 1",
"add 2",
"check 1",
"check 2",
"check 3",
"remove 2",
"check 1",
"check 2",
"toggle 3",
"check 1",
"check 2",
"check 3",
"check 4",
"all",
"check 10",
"check 20",
"toggle 10",
"remove 20",
"check 10",
"check 20",
"empty",
"check 1",
"toggle 1",
"check 1",
"toggle 1",
"check 1"
]

def test_case():
    assert 1
#     assert solution2(command)==[1,
# 1,
# 0,
# 1,
# 0,
# 1,
# 0,
# 1,
# 0,
# 1,
# 1,
# 0,
# 0,
# 0,
# 1,
# 0]
