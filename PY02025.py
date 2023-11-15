input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(*sorted(a & b))
print(*sorted(a - b))
print(*sorted(b - a))

# 5 6
# 1 2 3 4 5
# 3 4 5 6 7 8

