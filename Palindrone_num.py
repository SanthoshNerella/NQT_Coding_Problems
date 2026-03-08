n = int(input())
dup = n
rev_num = 0
while n > 0 :
    ld = n % 10
    rev_num = (rev_num * 10) + ld
    n //= 10
print(rev_num == dup)