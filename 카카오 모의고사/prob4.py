def solution(k, room_number):
    answer = []

    for i in room_number:
        if i in answer:
            rn = answer[answer.index(i)+1:]
            answer.append(min(rn)+1)
        else:
            answer.append(i)
    return answer