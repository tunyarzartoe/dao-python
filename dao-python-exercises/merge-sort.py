# マージソート
#merge sort
INF = 1000000001
count = 0


def print_array(a):
    print(*a)


def merge(a, left, mid, right):
    global count

    # それぞれの部分を新しい配列(リスト) l, r にコピー
    l = a[left:mid]
    r = a[mid:right]

    # 番兵を追加
    l.append(INF)
    r.append(INF)

    # lindex, rindex を 0 に初期化
    lindex, rindex = 0, 0
    for i in range(left, right):
        # l と r の先頭要素のうち l の先頭要素が小さいなら
        if l[lindex] < r[rindex]:
            # l の先頭要素を元の配列(リスト)に格納
            a[i] = l[lindex]
            # l の先頭を 1 つ進める
            lindex += 1
        else:
            # r の先頭要素を元の配列(リスト)に格納
            a[i] = r[rindex]
            # r の先頭を 1 つ進める
            rindex += 1
            count += 1


def merge_sort(a, left, right):
    # もし、left が right-1 以上なら終了
    if left >= right - 1:
        return

    # mid に (left+right)/2 を代入
    mid = (left + right) // 2

    # merge_sort(a, left, mid) と merge_sort(a, mid, right) を呼び出す
    merge_sort(a, left, mid)
    merge_sort(a, mid, right)

    # merge(a, left, mid, right) を呼び出す
    merge(a, left, mid, right)


n = int(input())
a = [int(x) for x in input().split()]

merge_sort(a, 0, n)

print_array(a)
print(count)
