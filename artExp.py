N = int(input())
arr = list(map(int, input().split()))
operand = ['*'] * (N - 1)
p = [[None] * 101 for i in range(N)]
p[0][arr[0]] = True
end = N - 1
for i in range(N - 1):
  if p[i][0]:
    end = i
    break
  for x in range(101):
    if p[i][x]:
      p[i + 1][(x + arr[i + 1]) % 101] = ('+', x)
      p[i + 1][(x + 101 - arr[i + 1]) % 101] = ('-', x)
      p[i + 1][(x * arr[i + 1]) % 101] = ('*', x)
x = 0
for i in range(end, 0, -1):
  operand[i - 1] = p[i][x][0]
  x = p[i][x][1]
print(''.join(str(x) for t in zip(arr, operand) for x in t) + str(arr[-1]))
