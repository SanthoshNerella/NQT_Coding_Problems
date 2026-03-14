n = int(input())
sum_of_natural_num = n * ( n + 1) // 2
print(sum_of_natural_num)

print("Another method using Loop")
m = int(input())
sum_natural = 0 
for i in range(1, m+1):
    sum_natural += i
print("Sum of n natural numbers is :", sum_natural)