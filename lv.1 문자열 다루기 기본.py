def solution(s):
    if len(s)==4 or len(s)==6:
        try:
            a = int(s)
            answer = True
        except:
            answer = False
        return answer
    else:
        return False