import math
arr = list(map(int, input().split()))
n = len(arr)
if n == 1 :
    print(arr[0])
else :
    total = 0
    for num in arr :
        total += num
    mean = math.floor(total / n)
    print(mean)