def print_array(a):
    # * = unpacking operator
    print(*a)


def insertion_sort(a, n):
    for i in range(1, n):
        # 先に a[i] を保存しておき、x とする
        x = a[i]
        # 挿入する位置を探すための変数 j を用意する
        j = i - 1

        # j が 0 以上かつ a[j] が x より大きい間
        while j >= 0 and x < a[j]:
            # a[j] を 1 つ右にずらす
            a[j+1] = a[j]
            # j を 1 減らす
            j -= 1

        # a[j+1] に x を挿入する
        a[j+1] = x

        print(*a)
        # print_array(a)


n = int(input())
a = [int(x) for x in input().split()]
insertion_sort(a, n)