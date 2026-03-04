arr = list(map(int, input().split()))
freq = {}
for num in arr :
    freq[num] = freq.get(num,0) + 1
result = sorted(arr , key =lambda x: (-freq[x], x))
print(result)