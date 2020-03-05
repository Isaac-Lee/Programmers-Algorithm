def solution(a, b):
    days = [31, 30]
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    day = b
    for m in range(a-1):
        if m == 1:
            day += 29
        elif m < 7:
            day += days[m%2]
        elif m >= 7:
            if m%2 == 0:
                day += days[1]
            else:
                day += days[0]
    return week[day%7]