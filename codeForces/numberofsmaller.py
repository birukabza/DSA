n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
res = []
while i < n and j < m:
    while i<n and b[j] > a[i]  :
        i+=1
    j+=1
    res.append(i)

while j < m:
    res.append(i)
    j+=1

print(*res)