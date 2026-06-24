# シェルソート
def insertion_sort(a, n, h):
    num_of_move = 0

    # i が h から n - 1 までのループを書く
    for i in range(h, n):
        # a[i] を x に保存する
        x = a[i]
        # 変数 j を用意する
        j = i - h

        # j が 0 以上で、a[j] が x より大きい間
        while j >= 0 and a[j] > x:
            # a[j] を h だけ右にずらす
            a[j+h] = a[j]
            # j を h だけ減らす
            j -= h

            num_of_move += 1

        # a[j+h] に x を代入する
        a[j+h] = x

    print(num_of_move)


def shell_sort(a, n, h, k):
    for i in range(k):
        # 間隔 h の挿入ソートを呼び出す
        insertion_sort(a, n, h[i])


n = int(input())
a = [int(x) for x in input().split()]
k = int(input())
h = [int(x) for x in input().split()]

shell_sort(a, n, h, k)