# 整数を受け取り、素因数分解をおこなって[素因数、個数]の連想配列(辞書)を返す関数
def factorize(n):
    primes = {}

    for i in range(2, int(n**0.5)+1):
        if n % i > 0:
            continue
        
        exp = 0
        while n % i == 0:
            exp += 1
            n //= i

        primes[i] = exp

    if n != 1:
        primes[n] =  1

    return primes


n = int(input())
table = factorize(n)
for prime in table:
    exp = table[prime]
    for _ in range(exp):
        print(prime)
