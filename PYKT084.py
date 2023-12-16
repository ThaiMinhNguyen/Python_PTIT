n = int(input())
ds = dict()
i = 1
s = input()
ds[s] = 0
n
while i < n:
    ss = input()
    if ss == '':
        s = input()
        ds[s] = 0
        i+=1
    else:
        ds[s]+=1
    i+=1
for k, v in ds.items():
    print(k + ":", v)
