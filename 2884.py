
H, M = map(int, input().split())

def timer(time, minute):

    if minute >= 45:
        minute -= 45
        return time, minute
    if minute < 45 and time >= 1:
        time -= 1
        minute += 15
        return time, minute
    if minute < 45 and time < 1:
        time = 23
        minute += 15
        return time, minute


A, B = map(int, timer(H, M))
print(A, B)
