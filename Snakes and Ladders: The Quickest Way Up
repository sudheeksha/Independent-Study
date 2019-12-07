def bfs(board):
    nexts = [(j, 1) for j in board[1][0] if j != 1]
    for i in nexts:
        board[i[0]][1] = False
        if len(board[i[0]][0]) == 1:
            i = (board[i[0]][0][0], i[1])
        if i[0] == 100:
            return i[1]
        nexts.extend([(j, i[1] + 1) for j in board[i[0]][0] if board[j][1]])



t = int(input())

for t_itr in range(t):
    n = int(input())

    board = dict()
    ladders = []

    for _ in range(n):
        ladders.append(list(map(int, input().rstrip().split())))

    m = int(input())

    snakes = []

    for _ in range(m):
        snakes.append(list(map(int, input().rstrip().split())))

    for i in ladders:
        board[i[0]] = [[i[1]], True]
    for i in snakes:
        board[i[0]] = [[i[1]], True]

    for i in range(1, 101):
        if not i in board.keys():
            board[i] = [[i for i in range(i + 1, i + 7) if i <= 100], True]

    res = bfs(board)
    if res == None:
        print(-1)
    else:
        print(res)
