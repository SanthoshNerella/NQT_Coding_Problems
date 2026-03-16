a , b , c = map(int,input().split())
if a > b and a > c:
    print("Greatest of theree numbers is: ", a)
elif b > c and b > a :
    print("greatest of three numbers is: ", b)
else:
    print("Greatest of three Numbers is: " , c)