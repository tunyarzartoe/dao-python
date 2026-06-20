def print_array(a):
    print(*a)


def bubble_sort(a, n):
    for i in range(n-1):
        # j が n-1 から i+1 までの for 文を用意する
        for j in range(n-1, i, -1):
            # A_{j-1} > A_j なら
            if a[j-1] > a[j]:
                # A_{j-1} と A_j を交換する
                a[j], a[j-1] = a[j-1], a[j]

        print_array(a)


n = int(input())
a = [int(x) for x in input().split()]
bubble_sort(a, n)