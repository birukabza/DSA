n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
sinks = []
sources = []
for i in range(n):
    sink = True
    for j in range(n):
        if matrix[i][j]==1:
            sink = False
    if sink:
        sinks.append(i+1)
for j in range(n):
    source = True
    for i in range(n):
        if matrix[i][j]==1:
            source = False
    if source:
        sources.append(j+1)



print(len(sources), *sources)           
print(len(sinks), *sinks)