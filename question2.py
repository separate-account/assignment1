def problem2():    
    n = int(input().strip())
    arr = list(map(int, input().split()))
    k = int(input().strip())

    rem = arr[0] % k
    for x in arr:
        if x % k != rem:
            print(-1)
            exit()

    arr.sort()
    median = arr[n // 2]

    ops = 0
    for x in arr:
        ops += abs(x - median) // k

    print(ops)

problem2()
