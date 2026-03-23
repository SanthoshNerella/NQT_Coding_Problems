arr = input().split()
def long_cmn_prefix(arr):
    if not arr:
        return ""
    prefix = arr[0]
    for s in arr[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
result = long_cmn_prefix(arr)
print(result)