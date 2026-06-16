# 区間の和を計算
n, x, y = map(int, input().split())
a = [int(x) for x in input().split()]

s = [0] * (n+1)

for i in range(n):
    s[i+1] = s[i] + a[i]
    
print(s[y] - s[x-1])    
    
