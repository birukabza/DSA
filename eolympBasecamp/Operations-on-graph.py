from collections import defaultdict


n = int(input())

op = int(input())
graph = defaultdict(list)

for _ in range(op):
    data = list(map(int, input().split()))

    if len(data) == 3:
        graph[data[1]].append(data[2])
        graph[data[2]].append(data[1])
    else:
        if data[1] in graph:
            print(*(graph[data[1]]))
        else:
            pass