
#!/usr/bin/python

def intervalSelection(intervals):
    intervals.sort()

    ans, threshold, rightest = 0, 0, 0
    for right, left in intervals:
        if left > threshold:
            ans += 1
            if left <= rightest:
                threshold = rightest
            rightest = right
    print(ans)


t = int(input())
for x in range(t):
    intervals = []
    n = int(input())
    for x in range(n):
        a, b = map(int, input().strip().split())
        intervals.append((b, a))
    intervalSelection(intervals)
