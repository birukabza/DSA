n = int(input())
count = 0
for _ in range(n):
    row = list(map(int, input().split()))
    for i in range(n):
        if row [i] == 1:
            count+=1
print(count//2)
