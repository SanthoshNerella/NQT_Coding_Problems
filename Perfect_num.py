n = int(input())
if n <= 0 :
    print(False)
else:
    sum_divisor = 0
    for i in range(1,n):
        if n % i == 0:
            sum_divisor += i
    print(sum_divisor == n)