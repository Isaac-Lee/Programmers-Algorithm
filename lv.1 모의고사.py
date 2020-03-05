def solution(answers):
    answer = []
    stu1 = [1, 2, 3, 4, 5]  # 5개
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개
    score = [0, 0, 0]
    for a in range(len(answers)):
        ans = answers[a]
        if stu1[a%5] == ans:
            score[0] += 1
        if stu2[a%8] == ans:
            score[1] += 1
        if stu3[a%10] == ans:
            score[2] += 1
    for i in range(3):
        if score[i] == max(score):
            print(i, score)
            answer.append(i+1)
    return answer