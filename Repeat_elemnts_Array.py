# arr = list(map(int, input().split()))
# seen = set()
# repeating_elemnts = set()
# for num in arr :
#     if num in seen :
#         repeating_elemnts.add(num)
#     else:
#         seen.add(num)

# print(",".join(map(str, sorted(repeating_elemnts))))
#----------------------------------------------------------------------------------
arr = list(map(int,input().split()))
freq = {}
for num in arr:
    freq[num] = freq.get(num,0) + 1
# for key , value in freq.items():
#     if value > 1:
#         print(key, end=" ")
print(" ".join(map(str,[key for key in freq if freq[key] > 1])))