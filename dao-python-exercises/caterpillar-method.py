n, k = map(int, input().split())
a = [int(x) for x in input().split()]

# 現在の右端を表す変数r,現在の総和を表す変数sum_value,答えを表す変数countを0で初期化
r, sum_value, count = 0, 0, 0
# 左端lを0からn-1まで繰り返す
for l in range(n):
    # rがnより小さく、sum_valueにa[r]を加えてもkを超えない間
    while r < n and sum_value+a[r] <= k:
        # sum_valueにa[r]を加えて右端rを1ずつ増やす
        sum_value += a[r]
        r += 1

    # r-lをcountに加える
    count += r - l

    # もしlがrと同じなら
    if l == r:
        # rを1増やす
        r += 1
    # そうでなければ
    else:
        # sum_valueからa[l]を引く
        sum_value -= a[l]

# countを出力
print(count)

#入力
# 5 2
# 1 1 2 2 2