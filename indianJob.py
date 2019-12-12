import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, G = list(map(int, sys.stdin.readline().split()))
        A = list(map(int, sys.stdin.readline().split()))

        if sum(A) > 2 * G:
            print('NO')

        else:
            DP = [[0] * (G + 1) for _ in range(N + 1)]

            for i in range(N + 1):
                for j in range(G + 1):
                    if i == 0 or j == 0:
                        DP[i][j] = 0
                    elif A[i - 1] > j:
                        DP[i][j] = DP[i - 1][j]
                    else:
                        DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - A[i - 1]] + A[i - 1])

            print('YES' if (sum(A) - DP[N][G] <= G) else 'NO')

