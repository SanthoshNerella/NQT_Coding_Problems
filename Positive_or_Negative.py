n = int(input())
if n == 0 :
    print("Zero")
elif n >> 31 & 1:
    print("Negative")
else:
    print("Positive")