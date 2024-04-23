from collections import defaultdict
n, m = map(int, input().split())
positions = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    positions[word].append(i)

for _ in range(m):
    word_b = input()
    if word_b in positions:
        print(*positions[word_b])
    else:
        print(-1)
