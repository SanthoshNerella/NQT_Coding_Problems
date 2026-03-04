line = input().strip("[]")
arr = list(map(int, line.split(",")))
if not arr :
    print(0)
else:
    curr_count = 1
    max_count = 1
    for i in range(1 , len(arr)):
        if arr[i] == arr[i - 1]:
            curr_count += 1
        else:
            curr_count = 1
        max_count = max(max_count,curr_count)
print(max_count)