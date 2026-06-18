def print_2d_array(a):
    for row in a:
        print(*row)

n, m = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(n)]

s = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        s[i + 1][j + 1] = (
            s[i + 1][j]
            + s[i][j + 1]
            - s[i][j]
            + a[i][j]
        )

print_2d_array(s)
