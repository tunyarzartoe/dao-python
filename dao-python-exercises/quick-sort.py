# クイックソート
count = 0
def print_array(a):
    print(*a)


def quick_sort(a, left, right):
    global count

    # もし left が right-1 以上なら終了
    if left >= right - 1:
        return

    # pivot に a[right-1] を代入
    pivot = a[right-1]

    # cur_index を left で初期化
    cur_index = left
    for i in range(left, right-1):
        # もし a[i] が pivot より小さいなら
        if a[i] < pivot:
            # a[cur_index] と a[i] を交換
            a[i], a[cur_index] = a[cur_index], a[i]

            # cur_index を 1 だけ増やす
            cur_index += 1
            count += 1

    # pivot と a[cur_index] を交換
    a[right-1], a[cur_index] = a[cur_index], pivot

    # quick_sort(a, left, cur_index) を呼び出す
    quick_sort(a, left, cur_index)
    # quick_sort(a, cur_index+1, right) を呼び出す
    quick_sort(a, cur_index+1, right)


n = int(input())
a = [int(x) for x in input().split()]

quick_sort(a, 0, n)

print_array(a)
print(count)