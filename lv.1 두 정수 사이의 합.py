def solution(a, b):
    answer = sum([n for n in range(min(a, b), max(a, b)+1)])
    return answer