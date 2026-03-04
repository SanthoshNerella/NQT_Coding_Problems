# line = input().strip("[]")
# arr = list(map(int, line.split(",")))
# unique_elmnts_array = [arr[0]]
# count = 0
# for i in range(1 ,len(arr)):
#     if arr[i] != arr[i-1]:
#         unique_elmnts_array.append(arr[i])
#         count += 1
# print(unique_elmnts_array)
# print("No of unique element ins arr is: " , len(unique_elmnts_array))
#-----------------------------------------------------------------------------
line = input().strip("[]")
arr = list(map(int, line.split(",")))
unique_elements = []
for num in arr :
    if num not in unique_elements :
        unique_elements.append(num)
print(unique_elements)
print("No of uique_elents in aray is: " , len(unique_elements))