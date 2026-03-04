# arr = list(map(int, input().split()))
# freq = {}
# for num in arr :
#     if num in freq :
#         freq[num] += 1
#     else:
#         freq[num] = 1
# for key, value in freq.items():
#     print(key, value)
# print("freq in sorted order: ")
# for key,value in sorted(freq.items()):
    # print(key,value)
#------------------------------------------------------------------------------
arr = list(map(int,input().split()))
freq = {}
print("initaly the dict is: " ,freq)
for num in arr :
    freq[num] = freq.get(num , 0) + 1
print(freq)
for key , value in freq.items():
    print(key,value)
print("dict after sortinf based on key: ")
for key, value in sorted(freq.items()):
    print(key,value)
print("dict after sorting values basd on value")
for key, value in sorted(freq.items(), key = lambda x : x[1]):
    print(key,value)
