arr = list(map(int, input().split()))
freq = {}
for num in arr :
    freq[num] = freq.get(num, 0) + 1
print("Non Repeating elements in an array: ")
print(" ".join(map(str,[key for key in freq if freq[key] == 1])))