def print_2d_array(a, n, m):
    print("\n".join(" ".join(map(str, x[:m])) for x in a[:n]))


n, m, x1, y1, x2, y2, x = map(int, input().split())

# 配列(リスト)aをサイズ(n+1)×(m+1)で用意
a = [[0] * (m+1) for _ in range(n+1)]

# a[x2+1][y2+1]にx,a[x2+1][y1]に-x,a[x1][y2+1]に-x,a[x1][y1]にxを加算
a[x2+1][y2+1] += x
a[x2+1][y1] -= x
a[x1][y2+1] -= x
a[x1][y1] += x

# iを0からn-1まで繰り返す
for i in range(n):
    # jを1からm-1まで繰り返す
    for j in range(1, m):
        # a[i][j]にa[i][j-1]を加算
        a[i][j] += a[i][j-1]

# jを0からm-1まで繰り返す
for j in range(m):
    # iを1からn-1まで繰り返す
    for i in range(1, n):
        # a[i][j]にa[i-1][j]を加算
        a[i][j] += a[i-1][j]

# aを出力
print_2d_array(a, n, m)

#入力
# 5 5 1 1 3 3 7
