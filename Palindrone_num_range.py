start = int(input("Enter start : "))
end = int(input("Enter end: "))
pal = []
for num in range(start,end + 1):
    n = num
    rev = 0
    while n > 0:
        ld = n % 10
        rev = rev * 10 + ld
        n //= 10
    if rev == num :
        pal.append(str(num))
print(" ".join(pal))