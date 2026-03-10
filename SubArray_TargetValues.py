line = input().strip("[]")
arr = list(map(int, line.split()))
target = int(input())
prefix_sum = 0
hsh_map = {0 : [-1]}
for i in range(len(arr)) :
    prefix_sum += arr[i]
    if prefix_sum - target in hsh_map :
        for start_index in hsh_map[prefix_sum - target] :
            print(arr[start_index + 1 : i + 1])
    if prefix_sum not in hsh_map :
        hsh_map[prefix_sum] = []
    hsh_map[prefix_sum].append(i)

