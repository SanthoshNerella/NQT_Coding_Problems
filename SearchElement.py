arr = list(map(int,input().split()))
k = int(input())
for i in range(len(arr)):
    if arr[i] == k :
        print("the targest is at index: " , i)
        break
