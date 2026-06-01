# n = int(input())
# a = [int(x) for x in input().split()]
# k = int(input())

# # 答えを出力する
# print(sorted(a, reverse=True)[k-1])

# 入力を受け取る
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

# 答えを保存する変数maximumを用意して適切な初期値で初期化
maximum = 101

# k回まわるループを書いて
for i in range(k):
    # 数列に含まれるmaximum未満の値の最大値を保存する変数next_maximumを用意して適切な初期値で初期化
    next_maximum = -101

    # 配列(リスト)の全要素をiterateするループを書いて
    for value in a:
        # next_maximumを更新する
        if next_maximum < value:
            next_maximum = value

    # maximumを更新する
    maximum = next_maximum

# 答えを出力する
print(maximum)


