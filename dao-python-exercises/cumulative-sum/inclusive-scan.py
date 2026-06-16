def print_array(a):
    print(*a)

n = int(input())
a = [int(x) for x in input().split()]

s = [0] * (n)

s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]

print_array(s)