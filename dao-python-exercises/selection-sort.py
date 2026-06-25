# 選択ソート
def print_array(a):
    print(*a)


def selection_sort(a, n):
    for i in range(n-1):
        # 変数 min_index を用意する
        min_index = i

        # j が i+1 から n-1 までのループを用意する
        for j in range(i+1, n):
            # A_j < A_{min_index} なら
            if a[j] < a[min_index]:
                # min_index を j に更新iする
                min_index = j

        # A_i と A_{min_index} を交換する
        a[i], a[min_index] = a[min_index], a[i]

        print_array(a)


n = int(input())
a = [int(x) for x in input().split()]
selection_sort(a, n)