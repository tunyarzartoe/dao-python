def print_2d_array(a):
    for row in a:
        print(*row)

n, m = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(n)]

s = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        s[i][j] = a[i][j]

        if i > 0:
            s[i][j] += s[i - 1][j]
        if j > 0:
            s[i][j] += s[i][j - 1]
        if i > 0 and j > 0:
            s[i][j] -= s[i - 1][j - 1]

print_2d_array(s)
