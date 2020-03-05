def solution(array, commands):
    answer = []
    for c in commands:
        n = array[c[0]:c[1]]
        n.sort()
        answer.append(n[c[2]])

    return answer