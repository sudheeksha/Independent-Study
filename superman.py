from collections import defaultdict


def solve(buildings, n, height, jump):
    prev = [0] * n
    max_height = [0]
    for h in range(1, height + 1):
        current = 0
        if jump >= h:
            next = 0
        else:
            next = max_height[-jump]
        for i, b in enumerate(buildings):
            prev = max(prev[i], next)
            prev[i] = prev + b[h]
            current = max(prev[i], current)
        max_height.append(current)
    return max_height[-1]


n, h, i = [int(s) for s in input().split()]
buildings = []
for _ in range(n):
    _, *floors = [int(s) for s in input().split()]
    b = defaultdict(int)
    for f in floors:
        b[f] += 1
    buildings.append(b)
print(solve(buildings, n, h, i))
