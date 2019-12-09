import sys
from functools import reduce
sys.setrecursionlimit(1000000)

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))


def is_alone(i, j):
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and b[ni][nj] != '.':
            return False
    return True


def fill(i, j, met):
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n:
            if b[ni][nj] != '.' and not v[ni][nj]:
                v[ni][nj] = True
                if b[ni][nj] != '?':
                    met.add(b[ni][nj])
                fill(ni, nj, met)
    return met


for _ in range(int(input())):
    n = int(input())
    b = [input().strip() for _ in range(n)]
    v = [[False for _ in range(n)] for _ in range(n)]
    ret = [1]
    for i in range(n):
        for j in range(n):
            if b[i][j] != '.' and not v[i][j]:
                v[i][j] = True
                if is_alone(i, j):
                    ret.append(3 if b[i][j] == '?' else 1)
                else:
                    met = fill(i, j, set() if b[i][j] == '?' else set(b[i][j]))
                    ret.append(0 if 'G' in met or len(met) == 2 else (2, 1)[len(met) > 0])
    print(reduce(lambda x, y: (x * y) % 1000000007, ret))
