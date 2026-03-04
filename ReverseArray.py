arr = list(map(int, input().split()))
#-------------------------------------------------------------------
# arr.reverse()
# print(arr)
#-----------------------------------------------------------------------
# reverse_Arr = []
# for i in range (len(arr) - 1 , -1 , -1):
#     reverse_Arr.append(arr[i])
# print(reverse_Arr)
#-------------------------------------------------------------------------------
# reverse_array = arr[::-1]
# print(reverse_array)
#------------------------------------------------------------------------------------
# reversed_arr = list(reversed(arr))
# print(reversed_arr)
#-------------------------------------------------------------------------------------
p1 = 0
p2 = len(arr) - 1
while p1 < p2 :
    arr[p1] , arr[p2] = arr[p2] , arr[p1]
    p1 +=1
    p2 -=1
print(arr)