def solution(source):
    source, dest =list(source), list(set(source))
    print(source, dest)
    res=''
    print(sorted(source)==sorted(dest))
    while sorted(source)!=sorted(dest):
        res+=''.join(sorted(dest))
        print(res)
        source = sourcecut(source,dest)
        dest = list(set(source))
    return res+''.join(source) if source else res

def sourcecut(source,dest):
    for i in dest:
        source.pop(source.index(i))
    return source
# def test_case():
#     assert solution("execute")=="cetuxee"
#     assert solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3) == 8
source="execute"

print(solution(source))