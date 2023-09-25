def divide_string(s):
    n = len(s)
    half = n // 2
    left = s[:half]
    right = s[half:]
    return left, right

def rotate_string(s):
    rotation = sum(ord(c) - ord('A') for c in s)
    rotated = ""
    for c in s:
        rotated += chr((ord(c) - ord('A') + rotation) % 26 + ord('A'))
    return rotated

def merge_strings(s1, s2):
    merged = ""
    for c1, c2 in zip(s1, s2):
        rotation = ord(c2) - ord('A')
        merged += chr((ord(c1) - ord('A') + rotation) % 26 + ord('A'))
    return merged

t = int(input())  # Số bộ test

for _ in range(t):
    s = input()  # Xâu ký tự cần mã hóa
    left, right = divide_string(s)
    rotated_left = rotate_string(left)
    rotated_right = rotate_string(right)
    result = merge_strings(rotated_left, rotated_right)
    print(result)

# 3
# EWPGAJRB
# BB
# TPQJDRJWSQXGRRIPXFMINTELHBJA