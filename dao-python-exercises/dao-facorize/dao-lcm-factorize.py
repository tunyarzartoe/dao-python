# 整数を受け取り、素因数分解をおこなって[素因数、個数]の連想配列(辞書)を返す関数
def factorize(n):
    primes = {}

    for i in range(2, n+1):
        if n % i > 0:
            continue

        exp = 0
        while n % i == 0:
            exp += 1
            n //= i

        primes[i] = exp

    if n != 1:
        primes[n] = 1

    return primes


def calc_lcm(a, b):
    table_a = factorize(a)
    table_b = factorize(b)
    table_lcm = {key: val for key, val in table_a.items()}

    for prime in table_b:
        exp = table_b[prime]
        if prime in table_a:
            exp = max(exp, table_a[prime])

        table_lcm[prime] = exp

    lcm = 1
    for factor in table_lcm:
        exp = table_lcm[factor]
        for _ in range(exp):
            lcm *= factor

    return lcm


a = 30
b = 12
gcd = calc_lcm(a, b)
print(f"{a} と {b} の最小公倍数は {gcd}")