arr = list(map(int,input().split()))
# arr.sort()
# print("the array after sorting the first half as ASc and second half as DESc")
# n = len(arr)
# arr[n//2:] = reversed(arr[n//2:])
# print(arr)
#----------------------------------------------------------------------------------------
n = len(arr)
mid = n // 2
arr.sort()
first_half = sorted(arr[:mid])
second_half = sorted(arr[mid:] , reverse = True)
result = first_half + second_half
print(result)