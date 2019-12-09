t = int(input())
for i in range(1, t + 1):
    n = int(input())
    row0 = input()
    row1 = input()
    row0_count = 0
    row1_count = 0
    result = 0
    for i in range(0, n):
        if row0[i] == '*':
            row0_count += 1
        if row1[i] == '*':
            row1_count += 1

    if row0_count > 0 and row1_count > 0:
        result = 1
        row0_count = 0
        row1_count = 0
        i = 0
        while i < n:
            if row0[i] == '*':
                row0_count += 1
            if row1[i] == '*':
                row1_count += 1

            if row0_count > 1 or row1_count > 1:
                i -= 1
                result += 1
                row0_count = 0
                row1_count = 0
            i += 1

    elif (row0_count > 0 and row1_count == 0) or (row0_count == 0 and row1_count > 0):
        result = max(row0_count, row1_count) - 1
    else:
        result = 0

    print(result)
