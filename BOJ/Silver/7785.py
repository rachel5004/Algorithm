def solution(lst):
    employees = {}
    for i in lst:
        name, status = i.split()
        employees[name]=status
    return sorted([k for k, v in employees.items() if v=="enter"],reverse=True)

def test_case():
    assert solution(["Baha enter","Askar enter","Baha leave","Artem enter"])==["Askar","Artem"]
    assert solution(["Baha enter", "Askar enter", "Baha leave", "Artem enter","Artem leave"]) == ["Askar"]
