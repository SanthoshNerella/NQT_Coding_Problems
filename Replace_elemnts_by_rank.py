arr = list(map(int,input().split()))
sorted_array = sorted(arr)
rank_map = {}
rank = 1
for num in sorted_array :
    if num not in rank_map :
        rank_map[num] = rank
        rank += 1
for i in range(len(arr)):
    arr[i] = rank_map[arr[i]]
print(" ".join(map(str,arr)))