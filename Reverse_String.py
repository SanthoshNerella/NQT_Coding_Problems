# s = input()
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string(s))
# ---------------------------------------------------------------------------------------------------------------------------
s = input()
def reverse_String(s):
    n = len(s)
    s = list(s)
    l = 0
    r = n - 1
    while l < r :
        s[l] , s[r] = s[r],s[l]
        l += 1
        r -= 1
    return ''.join(s)
print(reverse_String(s))