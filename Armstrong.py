n = int(input())
digits = len(str(n))
temp = n
total  = 0
while temp > 0:
    ld = temp % 10
    total += ld ** digits
    temp //= 10
if total == n:
    print(True)
else:
    print(False)