# 数列Aにkが何個含まれているかを求める問題
# 入力を受け取る
n = int(input())  # 要素数
A = list(map(int, input().split()))  # 数列A
k = int(input())  # 検索する値

# 数列Aにkが何個含まれているかを求める
count = 0
for element in A:
    if element == k:
        count += 1

# 結果を出力
print(count)

## 入力例
# 5
# 1 2 3 2 1
# 2
