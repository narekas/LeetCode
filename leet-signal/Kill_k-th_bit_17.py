def solution(n, k):
    return n if (n // 2 ** (k - 1)) % 2 == 0 else n - 2 ** (k - 1)
