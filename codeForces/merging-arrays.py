n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))




merged = [0] * (n + m)


i = 0
j = 0
k = 0


while i < n and j < m:

    if a[i] <= b[j]:
        merged[k] = a[i]
        i += 1
   
    else:
        merged[k] = b[j]
        j += 1
    k += 1

while i < n:
    merged[k] = a[i]
    i += 1
    k += 1


while j < m:
    merged[k] = b[j]
    j += 1
    k += 1


print(' '.join(map(str, merged)))