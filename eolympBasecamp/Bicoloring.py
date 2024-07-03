from collections import defaultdict
def solve(n):
    l = int(input())
    graph = defaultdict(list)
    for _ in range(l):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    color = [-1]*(n+1)
    def dfs(node):
        for nei in graph[node]:
            if color[nei] == -1:
                color[nei]  = 1-color[node]
                if not dfs(nei):
                    return False
            elif color[nei] == color[node]:
                return False
        return True

    for i in range(1,n+1):
        if color[i] == -1:
            color[i] = 0
            if not dfs(i):
                print("NOT BICOLOURABLE.")
                break
    else:
        print("BICOLOURABLE.")

while True:
    n = int(input())
    if n:
        solve(n)
    else:
        break


