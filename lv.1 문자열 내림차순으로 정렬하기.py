def solution(s):
    s = list(s)
    s.sort(reverse=True)
    print(s)
    answer = ''
    for c in s:
        answer += c
    return answer