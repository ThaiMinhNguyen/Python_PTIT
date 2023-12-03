res = dict()
for _ in range(int(input())):
    s = ''
    for i in input().lower() + ' ':
        if (i >= 'a' and i <= 'z'):
            s += i
        # elif (i >= '0' and i <= '9'):
        #     s = ''
        else:
            if (s != ''):
                if s in res:
                    res[s] += 1
                else:
                    res[s] = 1
                s = ''
res = dict(sorted(res.items(), key=lambda x : x[0]))
res = dict(sorted(res.items(), key=lambda x : x[1], reverse=True))
for k, v in res.items():
    print(k, v)
