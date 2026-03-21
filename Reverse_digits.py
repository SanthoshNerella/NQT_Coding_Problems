                #  when no leading zeroes
# ----------------------------------------------------------------------------------------------
# n = int(input())
# rev = 0
# while n > 0 :
#     lst_digt = n % 10
#     rev = (rev * 10) + lst_digt
#     n //= 10
# print(rev)
# ------------------------------------------------------------------------------------------------------
                #   when leading zeroes
# n = input()
# rev = n[::-1]
# print(rev)
# -----------------------------------------------------------------------------------------------------------
n = int(input())
negative = n < 0
rev = 0
n = abs(n)
if n == 0:
    rev = n
while n > 0 :
    last_dgt = n % 10
    rev = (rev * 10) + last_dgt
    n //= 10
if negative:
    rev = -rev
print(rev)
