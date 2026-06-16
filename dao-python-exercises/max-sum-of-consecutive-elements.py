n, k = map(int, input().split())
a = [int(x) for x in input().split()]

# 累積和を格納する長さn+1の配列(リスト)sを0で初期化
s = [0] * (n+1)
# iを0からn-1まで繰り返す
for i in range(n):
# s[i+1]にs[i]+a[i]を代入
    s[i+1] = s[i] + a[i]
# 暫定最大値を格納する変数max_sumを0で初期化
max_sum = 0
# iを0からn-kまで繰り返す
for i in range(n-k+1):
# もしs[i+k]-s[i]がmax_sumより大きければ
    if max_sum < s[i+k]-s[i]:
# max_sumをs[i+k]-s[i]で更新
        max_sum = s[i+k]-s[i]

# max_sumを出力
print(max_sum)