"""Kiểm tra số hoàn thiện (perfect) và số thịnh vượng (abundant).

"""

import math
def sum_proper_divisors(n: int) -> int:
    if n <= 1:
        return 0
    total = 1  # 1 là ước luôn có cho n > 1
    limit = int(math.isqrt(n))
    for d in range(2, limit + 1):
        if n % d == 0:
            total += d
            other = n // d
            if other != d:
                total += other
    return total


def is_perfect(n: int) -> bool:
    """True nếu n là số hoàn thiện (tổng ước nhỏ hơn n bằng n)."""
    if n <= 1:
        return False
    return sum_proper_divisors(n) == n


def is_abundant(n: int) -> bool:
    """True nếu n là số thịnh vượng (tổng ước nhỏ hơn n lớn hơn n)."""
    if n <= 1:
        return False
    return sum_proper_divisors(n) > n


def _demo():
    tests = [1, 2, 3, 6, 12, 18, 28]
    for t in tests:
        print(f"{t}: sum_divisors={sum_proper_divisors(t):>3}, perfect={is_perfect(t)}, abundant={is_abundant(t)}")


if __name__ == '__main__':
    _demo()
