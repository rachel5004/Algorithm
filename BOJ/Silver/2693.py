def solution(str):
    lst = list(map(int,str.split()))
    return sorted(lst)[-3]

def test_case():
    assert solution("1 2 3 4 5 6 7 8 9 1000") ==8
    assert solution("338 304 619 95 343 496 489 116 98 127") == 489
    assert solution("931 240 986 894 826 640 965 833 136 138") == 931
    assert solution("940 955 364 188 133 254 501 122 768 408") == 768
