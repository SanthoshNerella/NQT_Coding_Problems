arr = list(map(int, input().split()))
first_smallest = arr[0]
second_smallest = arr[0]
if len(arr) == 1:
    print(arr[0])
else:
    for num in arr :
        if num < first_smallest :
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest :
            second_smallest = num
if first_smallest == second_smallest :
    print(first_smallest)
else:
    print(second_smallest)