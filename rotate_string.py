a , b = input().split()
if len(a) != len(b):
    print("False")
else:
    temp = a + a
    if b in temp:
        print("True")
    else:
        print("False")