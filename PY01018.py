check = 1
P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while(check):
    st = input()
    if (st == '0'):
        break
    n = ''
    k, x = st.split()

    for i in x:
        z = P.find(i)
        n = n + P[(z+int(k)) % 28]
    print(n[::-1])