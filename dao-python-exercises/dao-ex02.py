# k 番目に大きい値を求める問題
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

index_of_k = 0
for i in range(n):
    if a[i] == k:
        index_of_k = i + 1      
        break
    
print(index_of_k)    