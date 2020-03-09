def solution(arr):
    answer = []
    for n in arr:
        if len(answer) == 0:
            answer.append(n)
        elif answer[len(answer)-1] != n:
            answer.append(n)

    return answer