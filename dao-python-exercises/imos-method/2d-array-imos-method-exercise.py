def print_2d_array(a, n, m):
    print("\n".join(" ".join(map(str, x[:m])) for x in a[:n]))


n, m, q = map(int, input().split())

# 差分配列を用意（端の処理用に+1）
a = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(q):
    x1, y1, x2, y2, x = map(int, input().split())

    a[x1][y1] += x
    a[x2 + 1][y1] -= x
    a[x1][y2 + 1] -= x
    a[x2 + 1][y2 + 1] += x

# 横方向の累積和
for i in range(n + 1):
    for j in range(1, m + 1):
        a[i][j] += a[i][j - 1]

# 縦方向の累積和
for i in range(1, n + 1):
    for j in range(m + 1):
        a[i][j] += a[i - 1][j]

print_2d_array(a, n, m)

#入力
# 5 5 1
# 1 1 3 3 7