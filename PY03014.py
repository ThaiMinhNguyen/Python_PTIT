for _ in range(int(input())):
    s = input()
    mo = 0
    dong = []
    for i in s:
        if i == '(':
            mo += 1
            print(mo, end= " ")
            dong.append(mo)
        elif i == ')':
            print(dong[-1], end=" ")
            dong.pop()
    print()