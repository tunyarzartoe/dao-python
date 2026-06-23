# 素数判定
# 整数を受け取り、素数かどうかを判定する関数
def primalityTest(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


n = 813
isPrime = primalityTest(n)
if isPrime:
    print(f"{n} は素数")
else:
    print(f"{n} は素数ではない")