def print_array(a, n):
    print(*a[:n])

n, l, r, x = map(int, input().split())

# 配列(リスト)aをサイズn+1で用意
a = [0] * (n+1)
# a[l]にxを、a[r+1]に-xを加算
a[l] += x
a[r+1] -= x

# iを1からn-1まで繰り返す
for i in range(1, n):
    # a[i]にa[i-1]を加算
    a[i] += a[i-1]

# aの先頭n要素を出力
print_array(a, n)

#入力
# 5 1 3 7