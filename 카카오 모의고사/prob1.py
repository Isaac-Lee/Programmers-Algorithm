def solution(board, moves):
    answer = 0

    basket = []
    for m in moves:
        for l in board:
            if l[m-1] > 0:
                basket.append(l[m-1])
                l[m-1] = 0
                break

    basket += [0] * len(board)
    b=0
    while True:
        if basket[b] == 0:
            break
        if basket[b] == basket[b + 1]:
            basket.pop(b)
            basket.pop(b)
            if b == 0:
                continue
            b -= 2
            answer += 2
        b += 1
    return answer
