#区間内の個数
n, x, y = map(int, input().split())
a = [int(x) for x in input().split()]

# 長さnの配列(リスト)bを用意
b = [0] * n
# iを0からn-1まで繰り返す
for i in range(n):
    # a[i]が偶数ならb[i]=1,奇数ならb[i]=0とする
    if a[i] % 2 == 0:
        b[i] = 1

# 累積和を格納する長さn+1の配列(リスト)sを0で初期化
s = [0] * (n+1)
# iを0からn-1まで繰り返す
for i in range(n):
    # s[i+1]にs[i]+b[i]を代入
    s[i+1] = s[i] + b[i]

# s[y+1]-s[x]を出力
print(s[y+1] - s[x])

# exercise
# n, x, y = map(int, input().split())
# a = [int(x) for x in input().split()]

# b = [0] * n
# # iを0からn-1まで繰り返す
# for i in range(n):
#     # a[i]が偶数ならb[i]=1,奇数ならb[i]=0とする
#     if a[i] % 2 == 0:
#         b[i] = 1

# # 累積和を格納する長さn+1の配列(リスト)sを0で初期化
# s = [0] * (n+1)
# # iを0からn-1まで繰り返す
# for i in range(n):
#     # s[i+1]にs[i]+b[i]を代入
#     s[i+1] = s[i] + b[i]
    
# even_count = s[y + 1] - s[x]
# odd_count = (y - x + 1) - even_count

# print(even_count)
# print(odd_count)
