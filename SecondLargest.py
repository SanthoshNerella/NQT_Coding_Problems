arr = list(map(int, input().split()))
first_largest = float('-inf')
second_largest = float('-inf')
if len(arr) == 1 :
    print(arr[0])
else:
    for ar in arr :
        if first_largest < ar :
            second_largest = first_largest
            first_largest = ar
        elif second_largest < ar < first_largest :
            second_largest = ar
if second_largest == float('-inf'):
    print(first_largest)
else:
    print(second_largest)