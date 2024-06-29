from collections import defaultdict
n = int(input())
adj = defaultdict(list)
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            adj[i+1].append(j+1)
    print(len(adj[i+1]), *(adj[i+1]))

