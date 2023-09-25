
def mul(a_x, a_y, b_x, b_y):
    result_x = (a_x * b_x + 5 * a_y * b_y) % 1000
    result_y = (a_x * b_y + a_y * b_x) % 1000
    return result_x, result_y

def pow(a_x, a_y, b):
    if b == 0:
        return 1, 0
    if b & 1:
        p_x, p_y = pow(a_x, a_y, b - 1)
        return mul(p_x, p_y, a_x, a_y)
    p_x, p_y = pow(a_x, a_y, b >> 1)
    return mul(p_x, p_y, p_x, p_y)

x = 3
y = 1

for t in range(int(input())):
    result_x, _ = pow(x, y, int(input()))
    print(f'Case #{t+1}: ', end='')
    print(str(result_x * 2 % 1000 - 1).zfill(3))