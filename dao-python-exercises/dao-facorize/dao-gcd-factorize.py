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


def calc_gcd(a, b):
    table_a = factorize(a)
    table_b = factorize(b)
    table_gcd = {}

    for prime in table_a:
        exp = table_a[prime]
        if prime in table_b:
            exp = min(exp, table_b[prime])
            table_gcd[prime] = exp

    gcd = 1
    for factor in table_gcd:
        exp = table_gcd[factor]
        for _ in range(exp):
            gcd *= factor

    return gcd


a = 30
b = 12
gcd = calc_gcd(a, b)
print(f"{a} と {b} の最大公約数は {gcd}")