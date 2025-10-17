t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    curr_size = n
    for i in range(k):
        last = a[curr_size - 1] if curr_size >= 1 else -1
        second_last = a[curr_size - 2] if curr_size >= 2 else -1
        pick = 1
        for x in range(1, 4):
            if x != last and x != second_last:
                pick = x
                break
        a.append(pick)
        curr_size += 1
        if i + 1 == k:
            print(pick)
        else:
            print(pick, end=' ')