m, n = map(int, input().split())
m = m - 1
sum_n = (n * (n + 1) // 2) ** 2
sum_m = (m * (m + 1) // 2) ** 2
sum_cubes = sum_n - sum_m
print(sum_cubes)