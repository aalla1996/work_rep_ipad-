# 1. Сумма нечётных от 1 до n включительно (два способа)

def sum_odds_for(n: int) -> int:
    s = 0
    for x in range(1, n + 1, 2):
        s += x
    return s

def sum_odds_formula(n: int) -> int:
    if n < 1:
        return 0
    m = (n + 1) // 2               # сколько нечётных в [1..n]
    return m * m                    # сумма первых m нечётных = m^2


# 2. Фильтр: оставить элементы, чьи квадраты < 100 (два способа)

def filter_lt100_loop(a: list[int]) -> list[int]:
    res = []
    for x in a:
        if x * x < 100:
            res.append(x)
    return res

def filter_lt100_compr(a: list[int]) -> list[int]:
    return [x for x in a if x * x < 100]


# 3. Мини-валидатор пароля: длина >= 8 и есть цифра

def check_password(s: str) -> str:
    has_digit = any(ch.isdigit() for ch in s)
    return "OK" if len(s) >= 8 and has_digit else "Weak"


# 4. Удалить подряд идущие дубликаты (сохранить первый из блока)

def dedup_consecutive(a: list[int]) -> list[int]:
    if not a:
        return []
    res = [a[0]]
    for x in a[1:]:
        if x != res[-1]:
            res.append(x)
    return res


# 5. Длина максимальной серии одинаковых элементов

def max_run_length(a: list[int]) -> int:
    if not a:
        return 0
    best = cur = 1
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            cur += 1
        else:
            if cur > best:
                best = cur
            cur = 1
    return best if best > cur else cur


# 6. Первое простое на [L, R]; если нет — None (использовать for-else)

def first_prime_in_range(L: int, R: int):
    if L > R:
        return None
    for n in range(max(L, 2), R + 1):
        for d in range(2, int(n ** 0.5) + 1):  # без isqrt
            if n % d == 0:
                break
        else:
            return n
    return None
# Печать: print(x if (x := first_prime_in_range(L,R)) is not None else "NONE")


# 7. K-разность: число пар (i<j) с |a[i]-a[j]| = k, O(n) времени/памяти

def k_diff_pairs(a: list[int], k: int) -> int:
    k = abs(k)
    # частоты вручную (без Counter)
    freq: dict[int, int] = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1

    if k == 0:
        # пары из одинаковых значений: C(c,2) для каждого значения
        return sum(c * (c - 1) // 2 for c in freq.values())

    total = 0
    for x, c in freq.items():
        total += c * freq.get(x + k, 0)  # считаем пары (x, x+k)
    return total


# 8. Слияние двух отсортированных списков (два указателя, без sort)

def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    i = j = 0
    res: list[int] = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    if i < len(a):
        res.extend(a[i:])
    if j < len(b):
        res.extend(b[j:])
    return res
# Сложность: O(len(a)+len(b)) времени; O(len(a)+len(b)) памяти под результат.


# 9. Почти возрастающая: можно удалить не более одного элемента

def almost_increasing(a: list[int]) -> bool:
    if len(a) <= 2:
        return True
    removed = 0
    prev_prev = float("-inf")
    prev = a[0]
    for i in range(1, len(a)):
        x = a[i]
        if x <= prev:
            removed += 1
            if removed > 1:
                return False
            # пытаемся "удалить" prev или x логически
            if x > prev_prev:
                prev = x          # удалить prev
            else:
                # удалить x — оставляем prev как есть
                pass
        else:
            prev_prev, prev = prev, x
    return True


# 10. Максимальная длина подпоследовательности с чередованием знаков (0 — разрыв)

def max_alt_sign_segment(a: list[int]) -> int:
    if not a:
        return 0
    best = 0
    cur = 0
    prev = 0  # предыдущее ненулевое по знаку
    for x in a:
        if x == 0:
            cur = 0
            prev = 0
            continue
        if cur == 0:
            cur = 1
            prev = x
        else:
            if prev * x < 0:   # знак сменился
                cur += 1
                prev = x
            else:
                cur = 1
                prev = x
        if cur > best:
            best = cur
    return best


if __name__ == "__main__":
    # 1
    assert sum_odds_for(7) == 16 and sum_odds_formula(7) == 16
    # 2
    assert filter_lt100_loop([9, 11, -12, 3]) == [9, 3]
    assert filter_lt100_compr([9, 11, -12, 3]) == [9, 3]
    # 3
    assert check_password("abc12345") == "OK" and check_password("abcdefg") == "Weak"
    # 4
    assert dedup_consecutive([1,1,2,2,2,3,1]) == [1,2,3,1]
    # 5
    assert max_run_length([1,1,2,2,2,3]) == 3 and max_run_length([]) == 0
    # 6
    p = first_prime_in_range(14, 20)
    assert p == 17
    # 7
    assert k_diff_pairs([1,5,3,4,2], 2) == 3  # пары: (1,3),(3,5),(2,4)
    assert k_diff_pairs([1,1,1], 0) == 3      # C(3,2)=3
    # 8
    assert merge_sorted([1,3,5], [2,2,4,6]) == [1,2,2,3,4,5,6]
    # 9
    assert almost_increasing([1,3,2,3]) is True
    assert almost_increasing([1,2,1,2]) is False
    # 10
    assert max_alt_sign_segment([1,-2,3,-4,5]) == 5
    assert max_alt_sign_segment([1,1,-1,-1,1]) == 2
    assert max_alt_sign_segment([0,1,-1,0,-2,2,-2,2,0]) == 4
