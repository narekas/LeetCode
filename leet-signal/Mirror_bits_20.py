def solution(a):
    m = 0

    while a > 0:
        bit = a % 2
        m = m * 2 + bit
        a = a // 2

    return m