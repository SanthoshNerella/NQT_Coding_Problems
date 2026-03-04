arr = list(map(int, input().split()))
n = len(arr)
arr.sort()
if n % 2 == 0 :
    left_value = (n // 2) - 1
    right_value = (n // 2) 
    Median = (arr[left_value] + arr[right_value]) / 2
    print(Median)
else:
    print(arr[n // 2])


a , b = map(int, input().split())
print("the value of a is : " , a)
print("the value of b is : " , b)