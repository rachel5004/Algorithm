def solution(info, query):
    infolist = sorted([i.split() for i in info], key=lambda x:int(x[-1]))
    answer = []
    for q in query:
        qlist = q.replace("and ", "").split()
        cnt=0
        for ilist in infolist:
            if int(qlist[-1]) > int(ilist[-1]): continue;
            flag = True
            for n in range(4):
                if qlist[n]!="-" and qlist[n]!=ilist[n]: flag=False; break;
            if flag: cnt+=1
        answer.append(cnt)
            
    return answer