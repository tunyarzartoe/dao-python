def binary_search(n, x, a):
    # 変数left,rightをそれぞれ0とn-1で初期化
    left, right = 0, n-1

    while right >= left:
        # 変数midに(left+right)/2を代入
        mid = (left + right) // 2

        # もしa[mid]がxに等しいなら
        if a[mid] == x:
            # trueを返す
            return True
        # もしa[mid]がxより大きいなら
        elif a[mid] > x:
            # rightにmid-1を代入
            right = mid - 1
        # そうでなければ
        else:
            # leftにmid+1を代入
            left = mid + 1

    # falseを返す
    return False


n, x = map(int, input().split())
a = [int(x) for x in input().split()]

print("Yes" if binary_search(n, x, a) else "No")

#入力
# 3 1
# 1 3 8