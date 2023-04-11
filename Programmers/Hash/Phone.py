def solution(phones):
    prefix = []
    for i in phones:
        for j in range(1,len(i)):
            prefix.append(i[:j])
    s = set(prefix)
    for i in phones:
        if i in s: return False
    return True
print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))