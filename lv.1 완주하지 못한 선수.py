import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

'''
예외처리문으로 해결
def solution(participant, completion):
    answer = ''
    try:
        for name in participant:
            completion.remove(name)
    except:
        answer = name
    return answer

정답코드이지만 시간초과로 실패
'''