# 素数を列挙するプログラム
def eratosthenes(n):
    isPrime = [True] * (n+1)
    isPrime[0], isPrime[1] = False, False
    for i in range(2, n+1):
        if not isPrime[i]:
            continue

        for j in range(i*2, n+1, i):
            isPrime[j] = False

    return isPrime


n = 813
isPrime = eratosthenes(n)
for i in range(1, n+1):
    if isPrime[i]:
        print(f"{i} は素数")
    else:
        print(f"{i} は素数ではない")