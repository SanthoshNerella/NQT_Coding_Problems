n , m = map(int,input().split())
primes = []
for i in range(n , m + 1):
    if i > 1:
        for r in range(2, int(i**0.5) + 1):
            if i % r == 0 :
                break
        else:
            primes.append(str(i))
print(" ".join(primes))