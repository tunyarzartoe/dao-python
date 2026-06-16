n, x, y = map(int, input().split())
a = [int(x) for x in input().split()]

# 累積和を格納する長さn+1の配列(リスト)sを0で初期化
s = [0] * (n+1)
# iを0からn-1まで繰り返す
for i in range(n):
    # s[i+1]にs[i]+a[i]を代入
    s[i+1] = s[i] + a[i]

# s[y+1]-s[x]を出力
print(s[y+1] - s[x])