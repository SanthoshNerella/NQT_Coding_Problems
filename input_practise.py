# n = int(input())
# print("you entered: ", n)
# # ---------------------------------------------------------------------
# m = int(input().strip())
# print("your taing inut using strip: ",m)
# ------------------------------------------------------------------------------------------------
# arr = list(map(int, input().split()))
# print(arr)
# -------------------------------------------------------------------------------------------------
# import sys
# data = list(map(int, sys.stdin.read().split()))
# # print(data)
# -----------------------------------------------------------------------------------------------
# s = input().strip()
# try:
#     num = int(s)
# except:
#     print("Invalid Input")
# --------------------------------------------------------------------------------------------------
# a , b = map(int,input().split())
# print(a)
# print(b)
# ----------------------------------------------------------------------------------------------------
# n = int(input())
# for i in range(n):
#     firstname,secondname,amount,bonus = input().split()
#     amount = int(amount)
#     bonus = int(bonus)
# ---------------------------------------------------------------------------------------------------------
# arr = list(map(int, input().strip('[]').split(",")))
# print(arr)
# --------------------------------------------------------------------------------------
# data = list(map(int,input().split()))
# n = data[0]
# arr = data[1:]
# print("size f array is : " , n)
# print(arr)
# -------------------------------------------------------------------------------------------
# data = input().strip()
# size_part , arr_part = data.split(",")
# arr = list(map(int, arr_part.strip().split()))
# n = int(size_part.strip())
# print(n)
# print(arr)
# ------------------------------------------------------------------------------------------------------------------------------------
sentence = input()
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word , 0) + 1
# for word , count in freq.items():
#     print(word,count)
sorted_items = sorted(freq.items(), key=lambda item: item[1])
for word, count in sorted_items:
    print(word,count)