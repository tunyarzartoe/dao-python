n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(n)]

# 累積和をとる二次元配列(リスト)sを0で初期化
s = [[0] * (m+1) for _ in range(n+1)]
# iが0からn-1まで、jが0からm-1までのループを回す
for i in range(n):
    for j in range(m):
        # s[i+1][j+1]=s[i+1][j]+s[i][j+1]-s[i][j]+a[i][j]とする
        s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + a[i][j]

# s[x2+1][y2+1]-s[x2+1][y1]-s[x1][y2+1]+s[x1][y1]を出力
print(s[x2+1][y2+1] - s[x2+1][y1] - s[x1][y2+1] + s[x1][y1])

# 3 3
# 0 0 2 2
# 8 0 0
# 0 1 0
# 0 0 3